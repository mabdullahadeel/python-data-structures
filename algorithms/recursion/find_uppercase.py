"""
    PROBLEM:
        Given a string, find the first occurrence of an uppercase letter
        and return the index of that letter. If no uppercase letters
        return None.
    Algorithm:
        1. Iterate through the string and check if the current
            character is uppercase. If so, return the tuple with given format -> (alphabet, index)
        2. Recursive approach
"""


def find_uppercase_iterative(input_str):
    for i in range(0, len(input_str)):
        if input_str[i].isupper():
            return input_str[i], i
    return None, None


def find_uppercase_recusive(input_str, idx=0):
    if input_str[idx].isupper():
        return input_str[idx], idx
    if idx == len(input_str) - 1:
        return None, None
    return find_uppercase_recusive(input_str, idx+1)