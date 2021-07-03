"""
    The algorithm solves the problem of arbitrary precision increment explained below.

    HOW IT WORKS?:
        Given: An array of non-negative digits that represent a decimal integer.

        Problem: Add one to the integer. Assume the solution still works even if implemented
                in a language with finite-precision arithmetic.
"""

def plus_one(array):
    array[-1] += 1

    for i in reversed(range(1, len(array))):
        if array[i] != 10:
            break
        array[i] = 0
        array[i - 1] += 1
    if array[0] == 10:
        array.append(0)

    return array