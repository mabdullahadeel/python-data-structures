"""
    Given two sorted arrays, A and B,
    determine their intersection. What
    elements are common to A and B?

    SIMPLE SOLUTION:
        res = set(A).intersection(B)
        Though the above solution works just fine even
        with unsorted arrays, but the solution given below
        is efficient.

    Assumption:
        - The arrays passed as argument to the function
        are sorted.
"""


def intersect_soted_arrays(array1, array2):
    i = j = 0
    intersections = []

    while i < len(array1) and j < len(array2):
        if array1[i] == array2[j]:
            if i == 0 or array1[i] != array1[i - 1]:    # handling duplicates
                intersections.append(array1[i])
            i += 1
            j += 1
        elif array1[i] < array2[j]:
            i += 1
        else:
            j += 1

    return intersections

