import time

"""
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
"""


def main():
    start = time.time()

    file = open('013.txt', 'r')

    list_of_numbers = []

    # To get the first ten digits of the sum is enough to add only the first 11 digits of the numbers
    list_of_numbers = [int(line[:11]) for line in file]
    sum_of_number = sum(list_of_numbers)

    print(
        "First 10 digits of the sum: " + str(sum_of_number)[:10])

    finish = time.time()

    print("Execution time : " +
          str(finish - start))


if __name__ == "__main__":
    main()
