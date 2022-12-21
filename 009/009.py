import time

"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a² + b² = c²
For example, 3² + 4² = 9 + 16 = 25 = 5².
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


def calculate_product(n):
    for a in range(1, n):
        for b in range(a + 1, n):
            c = 1000 - a - b
            if a*a + b*b == c*c:
                return a*b*c


def main():
    start = time.time()

    n = 1000

    product = calculate_product(n)

    print("Product of abc: " + str(product))

    finish = time.time()

    print("Execution time : " + str(finish - start))


if __name__ == "__main__":
    main()
