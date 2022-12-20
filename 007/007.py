import time

"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
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


def main():
    start = time.time()

    n = 10001

    prime_number = 13
    count = 6

    while count < n:
        prime_number += 2
        if is_prime(prime_number):
            count += 1

    print("10001st prime number: " + str(prime_number))

    finish = time.time()

    print("Execution time : " + str(finish - start))


if __name__ == "__main__":
    main()
