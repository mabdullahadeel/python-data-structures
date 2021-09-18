"""
    PROBLEM:
        write a function that takes a non-negative integer as
        argument and returns the largest integer whose square
        is less than or equal to the specified integer
    APPROACHES:
        - Iterative (can be expensive on large numbers)
        - Binary Search (used in this problem)
"""

def integer_square_root(k):
  low = 0
  high = k

  while low <= high:
    mid = (low + high)//2

    mid_sqr = mid * mid

    if mid_sqr <= k:
      low = mid + 1
    else:
      high = mid - 1
  return low - 1
