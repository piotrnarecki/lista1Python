def checkLength(username):
    if len(username) >= 3:  # sprawdza dlugosc loginu
        return True
    else:
        return False


def checkSpecialChars(username):
    import re
    string_check = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if (string_check.search(username) == None):  # sprawdza czy login nie zawiera znakow specjanych
        return True

    else:
        return False


def checkLowerAndUpperCase(username):
    if not username.islower():  # sprawdza czy wszystkie znaki to male litery
        return True
    else:
        return False


def main():
    username = raw_input('enter username : ')

    if checkLength(username):
        if checkSpecialChars(username):
            if checkLowerAndUpperCase(username):
                print ("great username ! ")
            else:
                print ("username should contain both upper and lower case")
        else:
            print ("username should not contain special characters")
    else:
        print ("username should contain at least 3 characters")


if __name__ == "__main__":
    main()
