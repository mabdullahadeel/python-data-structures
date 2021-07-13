"""
    PROBLEM:
        Given an array of nn distinct integers sorted in ascending order, write a function that
        returns a fixed point in the array. If there is not a fixed point, return None.
        -> A fixed point is an array index i such that Array[i] == i
    CONDITIONS:
        - Array is sorted
        - The list contains distinct elements
    APPROACHES:
        - Iterative O(n)
        - Binary Search O(log n) -> used in this problem
"""

# Native Approach (iterative)
# Time Complexity: O(n)
# Space Complexity: O(1)
def find_fixed_point_iterative(array):
    for i in range(len(array) - 1):
        if array[i] == i:
            return array[i]
    return None

def find_fixed_point(array):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid_point = (low + high)//2

        if array[mid_point] < mid_point:
            # since the array is sorted all the values to the left should not qualify
            low = mid_point + 1
        elif array[mid_point] > mid_point:
            # since array is sorted, all the elements to the right should not qualify
            high = mid_point - 1
        else:
            return array[mid_point]

    return None