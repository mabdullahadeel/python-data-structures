"""
    PROBLEM:
        Given a sorted array, and a target number, find a number in the array
        which is closest to the target number.
    SOLUTION:
        - Here we'll use binary search
    CONSTRAINTS:
        - Array may contain duplicate values
    EXAMPLES:
         -  Input : arr[] = {1, 2, 4, 5, 6, 6, 8, 9}
            Target number = 11
            Output : 9
            9 is closest to 11 in given array
         -  Input :arr[] = {2, 5, 6, 7, 8, 8, 9};
            Target number = 4
            Output : 5
    POTENTIAL SOLUTIONS:
        - ITERATIVE -> O(n)
        - Binary Search -> O(log n) -> selected for this problem
"""

def find_closest_num(array, target):
    min_diff = min_difference_right = min_difference_left = float("inf")
    array_len = len(array)
    low = 0
    high = array_len - 1
    closest_number = None

    # Edge cases
    if len(array) == 0:
        return None
    if len(array) == 1:
        return array[0]

    while low <= high:
        mid_point = (low + high)//2

        # preventing exceeding boundaries from both sides of the array
        if mid_point + 1 < array_len:       # right side check
            min_difference_right = abs(array[mid_point + 1] - target)
        if mid_point > 0:                   # left side check
            min_difference_left = abs(array[mid_point - 1] - target)


        # comparing the difference values with the ones seen already
        if min_difference_left < min_diff:
            min_diff = min_difference_left
            closest_number = array[mid_point - 1]
        if min_difference_right < min_diff:
            min_diff = min_difference_right
            closest_number = array[mid_point + 1]

        # Moving the mid-point to appropriate place as it is done its thing for the loop instance
        # using BS concepts
        if array[mid_point] < target:
            low = mid_point + 1             # move to right
        elif array[mid_point] > target:
            high = mid_point - 1            # move to left
            if high < 0:
                return array[mid_point]
        # If the element itself is the target, the closest
        # number to it is itself. Return the number.
        else:
            return array[mid_point]

    return closest_number




