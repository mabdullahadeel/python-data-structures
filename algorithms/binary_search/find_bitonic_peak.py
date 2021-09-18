"""
    PROBLEM:
        given a bitonically sorted array, find the bitonic peak
        -> A bitonic sequence is a sequence of integers such that:
            x_0 < ... < x_k > ... > x_{n-1}
            for some kk, 0 <= kk < nn
        EXAMPLE:
            1, 2, 3, 4, 5, 4, 3, 2, 1 (is bitonically sorted with '5' as peak)
    ASSUMPTIONS:
        - Peak will always exist
        - For bitonic peak, the element to the right and left should be less than the peak
    APPROACHES:
        - Iterative
        - Binary Search (used in this problem)
"""


def find_bitonic_peak(array):
    low = 0
    high = len(array) - 1

    # To qualify for bitonic, these must be three elements in array
    if len(array) < 3:
        return None

    while low <= high:
        mid_point = (low + high)//2

        mid_left = array[mid_point - 1] if mid_point - 1 > 0 else float("-inf")
        mid_right = array[mid_point + 1] if mid_point + 1 < len(array) else float("inf")

        if (mid_left < array[mid_point]) and (mid_right > array[mid_point]):
            low = mid_point + 1         # the peak should be on the right
        elif (mid_left > array[mid_point]) and (mid_right < array[mid_point]):
            high = mid_point - 1        # the peak is on the left side of the mid point
        elif mid_left < array[mid_point] and mid_right < array[mid_point]:
            return array[mid_point]

    return None