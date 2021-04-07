
def addItem(item, quantity, filePath):
    # dodaje pozycje do listy
    itemLine = item + " " + str(quantity)

    file = open(filePath, "a")
    file.write(itemLine + "\n")
    file.close()
    print 'item added'

def createGroceryList(filePath):
    # tworzy pozycje na liscie zakupow z wejscia
    item = 'input'
    while item.lower() != 'q':
        try:
            item = raw_input('enter item (enter q to close program) ')
            if item.lower() != 'q' and not item.isdigit():
                quantity = int(raw_input('enter quantity '))
                addItem(item, quantity, filePath)
            else:
                print 'item should be not a number'
        except ValueError:
            print '1st argument is item , 2nd is quantity '
    else:
        print 'shutting down program'


def createNewFile(filePath):
    import os

    path = filePath
    # path = "/Users/piotrnarecki/Desktop/groceryList1.txt"

    with open(os.path.join(path), 'w+') as fp:
        pass

    with open('myfile.txt', 'w+') as fp:
        pass

    print ('a new list has been created')


def main():
    import sys

    if len(sys.argv) is 2:
    #sprawdza czy plik istnieje
        try:
            filePath = (sys.argv[1])
            # filePath = "/Users/piotrnarecki/Desktop/groceryList1.txt"
            file = open(filePath, "rt")
            print ('this list already exist')


        except IOError:
            createNewFile(filePath)

        createGroceryList(filePath)

    else:
        print ('enter only filepath')


if __name__ == "__main__":
    main()
