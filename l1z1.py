import math


def main():
    import sys

    if len(sys.argv) is 7:

        try:
            x1 = float(sys.argv[1])
            y1 = float(sys.argv[2])
            z1 = float(sys.argv[3])

            x2 = float(sys.argv[4])
            y2 = float(sys.argv[5])
            z2 = float(sys.argv[6])

            print ('1st coordinates:', x1, y1, z1)
            print ('2nd coordinates:', x2, y2, z2)

            distance = math.sqrt((x2 - x1) ** 2 + (y1 - y2) ** 2 + (z2 - z1) ** 2)

            result = '{0:.2f}'.format(distance)
            print ('Distance:', result)
        except ValueError:
            print ('Coordinates are numbers!')
    else:
        print ('Not enough arguments')
        print ('size ', len(sys.argv))


if __name__ == "__main__":
    main()
