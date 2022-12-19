import time

"""
Each new term in the Fibonacci sequence is generated by adding the previous
two terms. By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence whose values do not exceed
four million, find the sum of the even-valued terms.
"""


def calculate_fibonacci(n):

    # Every third Fibonacci term is even

    x = y = 1
    fib = x + y
    sum = 0
    while fib < n:
        sum += fib
        x = y + fib
        y = x + fib
        fib = x + y
    return sum


def main():

    start_time = time.time()

    n = 4000000

    sum = calculate_fibonacci(n)

    print("Sum = " + str(sum))

    finish_time = time.time()

    print("Execution time : " + str(finish_time - start_time))


if __name__ == "__main__":
    main()