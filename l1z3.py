def displayData(day, month, year, sex):  # wyswietla date urodzenia i plec
    from datetime import datetime

    dateOfBirth = str(day) + str(month) + str(year)
    dateOfBirth = datetime.strptime(dateOfBirth, '%d%m%Y').strftime('%d-%m-%Y')

    displayedData = dateOfBirth + " " + sex
    print (displayedData)


def peselToList(pesel):  # zamienia numer PESEL na liste cyfr
    peselList = [None] * 11
    pesel = str(pesel)
    for i in range(0, len(peselList)):
        peselList.__setitem__(i, pesel[i])
    return peselList


def check(peselList):  # sprawdza z uzyciem sumy kontrolnej czy numer PESEL jest poprawny
    checksumList = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    checksum = 0
    for i in range(0, len(checksumList)):
        checksum = checksum + checksumList.__getitem__(i) * int(peselList.__getitem__(i))

    result = checksum % 10
    result = (10 - result) % 10

    if result is int(peselList.__getitem__(len(peselList) - 1)):
        return True
    else:
        return False


def analyze(peselList):  # odczytuje z numeru PESEL date urodzenia i plec
    year = 1900 + int(peselList.__getitem__(0)) * 10 + int(peselList.__getitem__(1))

    month = int(peselList.__getitem__(2)) * 10 + int(peselList.__getitem__(3))

    if 12 < month <= 32:
        month = month - 20
        year = year + 100

    day = int(peselList.__getitem__(4)) * 10 + int(peselList.__getitem__(5))

    sexNumber = int(peselList.__getitem__(9))
    if (sexNumber % 2) == 0:
        sex = "K"
    else:
        sex = "M"

    displayData(day, month, year, sex)


def main():
    import sys

    if len(sys.argv) is 2:

        if len(sys.argv[1]) is 11:

            try:
                pesel = int(sys.argv[1])

                print(pesel)
                peselList = peselToList(pesel)

                if check(peselList):

                    analyze(peselList)
                else:
                    print ("wrong PESEL !")

            except ValueError:
                print ('PESEL contain 11 digit')

        else:
            print ('PESEL contain 11 digit')

    else:
        print ('You should enter only PESEL !')


if __name__ == "__main__":
    main()
