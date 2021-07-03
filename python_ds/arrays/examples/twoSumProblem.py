"""
    Given an array of integers, return `True` or `False` if array has two numbers
    that add up to a specific target.

    Assumption:
        - Each input has only one solution so the algorithm will return on the first result

    APPROACHES:
        There are three solution provided to this problem as different methods of the given
        class. All the approaches there have been described as well.
"""

class TwoSumProblem:
    def __init__(self, array, target):
        self.array = array
        self.target = target


    def two_sum_brute_force(self):
        """
            This function use the brute force approach to get to the solution
            -> Time Complexity: O(n^2)
            -> Space Complexity: O(1)
        """
        for i in range(len(self.array) - 1):
            for j in range(i + 1, len(self.array)):
                if self.array[i] + self.array[j] == self.target:
                    return True

        return False


    def two_sum_hash_table(self):
        """
            This function uses has table to keep track of entries and get to the result
            -> Time Complexity: O(n)
            -> Space Complexity: O(n)
        """
        hash_table = dict()

        for i in range(len(self.array)):
            if self.array[i] in hash_table:
                return True
            else:
                hash_table[self.target - self.array[i]] = self.array[i]


    def two_sum_both_ways_track(self):
        """
            Here, we have two indices that we keep track of,
            one at the front and one at the back. We move either
            the left or right indices based on whether the sum
            of the elements at these indices is either greater
            than or less than the target element.

            -> Time Complexity: O(n)
            -> Space Complexity: O(1)

            Assumption:
                - This approach assumes that the array passed is sorted
        """
        i = 0
        j = len(self.array) - 1

        while i < j:
            if self.array[i] + self.array[j] == self.target:
                return True
            elif self.array[i] + self.array[j] < self.target:
                i += 1
            else:
                j -= 1

        return False