"""
    This is an algorithm to code an array advance game using efficient approach.

    THE PROBLEM:
        Is it possible to advance from the start of the array to the
        last element given that the maximum you can advance from a
        position is based on the value of the array at the index you
        are currently present on?
        (In short you need to reach the end of the list if possible starting from the beginning)

    APPROACHES:
        - Greedy Approach -> Move as much as possible i-e always move next depending upon
          the value of index you are currently on.
          DOESN'T WORK ALL THE TIME
        - Iterative Approach -> Iterate over the array and keep track of furthest you can reach
"""


def array_advance(array):
    furthest_reached = 0
    last_idx = len(array) - 1
    i = 0

    while (i <= furthest_reached) and (furthest_reached < last_idx):
        furthest_reached = max(furthest_reached, array[i] + i)
        i += 1

    return furthest_reached >= last_idx