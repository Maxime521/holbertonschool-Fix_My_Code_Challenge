#!/usr/bin/python3
""" FizzBuzz
"""
import sys


def fizzbuzz(n):
    """
    Prints numbers from 1 to n with the following substitutions:
    - Multiples of 3 are replaced by 'Fizz'
    - Multiples of 5 are replaced by 'Buzz'
    - Multiples of both 3 and 5 are replaced by 'FizzBuzz'

    Parameter:
    n (int): the upper limit of the sequence (inclusive)
    """
    if n < 1:
        return

    tmp_result = []
    for i in range(1, n + 1):
         if (i % 3) == 0 and (i % 5) != 0:
            tmp_result.append("Fizz")
         elif (i % 3) == 0 and (i % 5) == 0:
            tmp_result.append("FizzBuzz")
         elif (i % 5) == 0:
            tmp_result.append("Buzz")
         else:
            tmp_result.append(str(i))
    print(" ".join(tmp_result))


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print("Missing number")
        print("Usage: ./0-fizzbuzz.py <number>")
        print("Example: ./0-fizzbuzz.py 50")
        sys.exit(1)

    number = int(sys.argv[1])
    fizzbuzz(number)
