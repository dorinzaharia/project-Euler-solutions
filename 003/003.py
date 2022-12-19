import time

"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
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


def largest_number(n):
    divisor = 2
    largest_prime_number = 2

    while n > 1:
        if n % divisor == 0:
            n /= divisor
            if largest_prime_number < divisor and is_prime(divisor):
                largest_prime_number = divisor
            divisor = 2
        else:
            divisor += 1
    return largest_prime_number


def main():
    start_time = time.time()
    n = 600851475143
    print("Largest prime number: " + str(largest_number(n)))

    finish_time = time.time()
    print("Execution time : " + str(finish_time - start_time))


if __name__ == "__main__":
    main()
