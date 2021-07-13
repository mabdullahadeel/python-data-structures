"""
    PROBLEM:
        Given an array of sorted integers and a key and
        returns the index of the first occurrence of that
        key from the array
    EXAMPLE:
        [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
        Output: 3
        target: 108
    APPROACHES:
        - Iterative O(n)
        - Binary Search O(log n) -> used to solve this problem
"""

# Iterative_approach
# time: O(n)
# space: O(1)
def find_first_ent_with_duplicates_iterative(array, target):
    for i in range(len(array) - 1):
        if array[i] == target:
            return i
    return None


def find_first_ent_with_duplicates(array, target):
    low = 0
    high = len(array) - 1

    # since array is sorted, applying binary search
    while low <= high:
        mid = (low + high)//2

        if array[mid] < target:
            low = mid + 1
        elif array[mid] > target:
            high = mid - 1
        else:
            if mid - 1 < 0:
                return mid
            if array[mid - 1] != target:
                return mid
            high = mid - 1