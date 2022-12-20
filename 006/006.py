import time

"""
The sum of the squares of the first ten natural numbers is
1² + 2² +...+10² = 385
The square of the sum of the first ten natural numbers is
(1 + 2 +...+10)² = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
3025 - 385 = 2640
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""


def main():

    start = time.time()

    n = 100

    # sum of the squares of first n number s = (n * (n + 1) * (2 * n + 1)) / 6
    sum_of_squares = (n * (n + 1) * (2 * n + 1)) / 6

    # sum of first n numbers s = n * ( n + 1) / 2
    square_of_sum = pow(n * (n + 1) / 2, 2)

    print("Difference: " + str(int(square_of_sum - sum_of_squares)))

    finish = time.time()

    print("Execution time : " + str(finish - start))


if __name__ == "__main__":
    main()
