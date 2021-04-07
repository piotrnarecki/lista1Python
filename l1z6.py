def countParagraphs(filePath):
    file = open(filePath, "rt")
    paragraphsCount = 0
    data = file.read()
    lines = data.split("\n")

    for i in lines:
        if i:
            paragraphsCount += 1
    print("This is the number of lines in the file")

    file.close()
    return paragraphsCount


def countWords(filePath):
    file = open(filePath, "rt")
    data = file.read()
    words = data.split()
    wordsCount = len(words)

    file.close()
    return wordsCount


def countCharacters(filePath):
    file = open(filePath, "rt")
    data = file.read().replace(" ", "")
    charactersCount = len(data)
    file.close()
    return charactersCount


def main():
    import sys

    if len(sys.argv) is 2:

        try:
            filePath = (sys.argv[1])
            # filePath = "/Users/piotrnarecki/Desktop/text1.txt"

            paragraphs = countParagraphs(filePath)
            words = countWords(filePath)

            characters = countCharacters(filePath)

            print "paragraphs:", paragraphs, " words:", words, " characters:", characters


        except IOError:
            print ('this file does not exist')
    else:
        print ('enter only filepath')


if __name__ == "__main__":
    main()
