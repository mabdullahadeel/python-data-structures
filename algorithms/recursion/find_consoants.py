"""
    PROBLEM:
        Given a string, find the number of consonants
        in the string.
    APPROACHES:
        - Iterative
        - Recursive
"""


vowls = "aeious"

def find_consonants_iterative(string):
    count = 0

    for char in string:
        if char not in vowls and char.isalpha():
            count += 1
    return count


def find_consonants_recursive(input_string):
    if not input_string:
        return 0

    if input_string[0].lower() not in vowls and input_string[0].isalpha():
        return 1 + find_consonants_recursive(input_string[1:])
    else:
        return find_consonants_recursive(input_string[1:])

