import math


def fibonacci(m, n):  # oblicza roznice miedzy sumami n i m wyrazow ciagu

    m1, m2 = 0, 1
    counter = 0
    sumM = 0
    sumN = 0

    while counter < m:  # oblicza m-ty wyraz ciagu i sume m wyrazow ciagu
        mth = m1 + m2
        m1 = m2
        m2 = mth
        counter += 1
        sumM = sumM + m1

    n1 = m1
    n2 = m2

    while counter < n:  # oblicza n-ty wyraz ciagu i sume n wyrazow ciagu
        nth = m1 + mth
        n1 = n2
        n2 = nth
        counter += 1
        sumN = sumN + n1

    sum = sumN - sumM
    return sum


def main():
    import sys

    if len(sys.argv) is 3:

        try:
            m = int(sys.argv[1])
            n = int(sys.argv[2])

            if n > m > 0:
                result = fibonacci(m, n)
                print (result)
            else:
                print ("m should be lower than n and greater than 0")

        except ValueError:
            print ('You should enter numbers')
    else:
        print ('Not enough arguments')


if __name__ == "__main__":
    main()
