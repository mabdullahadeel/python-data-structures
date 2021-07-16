"""
    PROBLEM:
        Given an array return the index of the
        smallest element of the cyclically shifted array.

        - An array is “cyclically shifted” if it is possible
            to shift its entries cyclically so that it becomes sorted.
    APPROACHES:
        - iterative
        - Binary Search (used in this problem)
"""


def find(A):
    low = 0
    high = len(A) - 1

    while low < high:
        mid = (low + high)//2

        if A[mid] > A[high]:
            low = mid + 1
        elif A[mid] <= A[high]:
            high = mid

    return low