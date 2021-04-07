def wordsToList(file):
    data = file.read()
    wordsList = data.split()
    file.close()
    return wordsList


def compareFiles(filePath1, filePath2):
    repeatedWordsList = []

    file1 = open(filePath1, "rt")
    file2 = open(filePath2, "rt")

    wordsList1 = wordsToList(file1)
    wordsList2 = wordsToList(file2)

    for i in range(0, len(wordsList1)):
        for j in range(0, len(wordsList2)):
            if (wordsList1.__getitem__(i) == wordsList2.__getitem__(j)):
                repeatedWordsList.append(wordsList1.__getitem__(i))

    repeatedWordsList.sort()
    return repeatedWordsList


def main():
    import sys

    if len(sys.argv) is 3:

        try:
            filePath1 = (sys.argv[1])
            # filePath1 = "/Users/piotrnarecki/Desktop/text1.txt"

        except IOError:
            print ('1st file does not exist')

        try:
            filePath2 = (sys.argv[2])
            # filePath2 = "/Users/piotrnarecki/Desktop/text2.txt"


        except IOError:
            print ('2nd file does not exist')

        try:
            repeatedWords = compareFiles(filePath1, filePath2)
            print 'repeated words:', repeatedWords
        except IOError:
            print ('something goes wrong')

    else:
        print ('enter only 2 filepaths')


if __name__ == "__main__":
    main()
