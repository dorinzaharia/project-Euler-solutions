import time

"""
A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""


def is_palindrome(number):
    copy_of_number = number
    reversed_number = 0

    while copy_of_number > 1:
        reversed_number = reversed_number * 10 + int(copy_of_number % 10)
        copy_of_number /= 10

    if reversed_number == number:
        return True
    return False


def largest_palindrome():
    # Largest 3-digit number 999, smallest 101
    largest_palindrome = 1
    for i in range(999, 101, -1):
        for j in range(i, 101, -1):
            if is_palindrome(i * j) and i * j > largest_palindrome:
                largest_palindrome = i * j
    return largest_palindrome


def main():

    start = time.time()

    print("Largest palindrome: " + str(largest_palindrome()))

    finish = time.time()

    print("Execution time : " + str(finish - start))


if __name__ == "__main__":
    main()
