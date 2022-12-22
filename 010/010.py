import time
import math

"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""

# This can be resolved with Sieve of Eratosthenes algorithm
# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes


def main():
    start = time.time()

    n = 2000000

    sum = 0

    array_of_numbers = list(range(2, n))

    for i in range(2, int(math.sqrt(n))):
        if array_of_numbers[i - 2] != 0:
            j = i
            while i * j < n:
                array_of_numbers[i * j - 2] = 0
                j += 1

    for i in range(2, n):
        if array_of_numbers[i - 2]:
            sum += array_of_numbers[i - 2]

    print("Sum of primes: " + str(sum))

    finish = time.time()

    print("Execution time : " + str(finish - start))


if __name__ == "__main__":
    main()
