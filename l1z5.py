def cToF(temp):  # zamiana C na F
    convertedTemp = temp * 1.8 + 32
    return convertedTemp


def fToC(temp):  # zamiana F na C
    convertedTemp = (temp - 32) / 1.8
    return convertedTemp

def conversion(conversionTo,temp):
    if conversionTo == "c":
        convertedTemp = round(fToC(temp), 2)
        print (str(temp) + " C = " + str(convertedTemp) + " F")
    elif conversionTo == "f":
        convertedTemp = round(cToF(temp), 2)
        print(str(temp) + " F = " + str(convertedTemp) + " C")
    else:
        print("first argument should be letter C or F")


def main():
    import sys

    if len(sys.argv) is 3:

        try:
            conversionTo = (sys.argv[1]).lower()
            temp = float(sys.argv[2])
            conversion(conversionTo, temp)

        except ValueError:
            print ('you should enter letter C or F and number')
    else:
        print ('not enough arguments')


if __name__ == "__main__":
    main()
