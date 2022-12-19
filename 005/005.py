import time

"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""


# Check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n / 2) + 1, 2):
        if n % i == 0:
            return False
    return True


def smallest_multiple(n):
    """
    To calculate the smallest positive number that is evenly divisible by all of the numbers from 1 to 20 is enough to calculate multiple of all prime numbers raised
    to a maximal power in which this number is smaller than our range
    """

    smallest_multiple = 1

    for i in range(2, n):
        if is_prime(i):
            num = i
            while num * i < n:
                num *= i
            smallest_multiple *= num
    return smallest_multiple


def main():

    start = time.time()

    n = 20
    print("Smallest multiple: " + str(smallest_multiple(n)))

    finish = time.time()

    print("Execution time : " + str(finish - start))


if __name__ == "__main__":
    main()
