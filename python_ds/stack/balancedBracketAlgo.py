from .stack import Stack


"""
The function `are_parenthesis_balanced` is a simple function
that checks if a given string has balanced bracket pair and
returns a boolean respectively
"""


def is_valid_pair(opening, closing):
	# Process the brackets and see if they are valid pair
	pairs = {"(": ")", "[": "]", "{": "}"}

	result = False
	if opening in pairs.keys():
		result = pairs[opening] == closing

	return result

def are_parenthesis_balanced(paren_str):
	stack = Stack()
	is_balanced = True
	index = 0

	while index < len(paren_str) and is_balanced:
		paren = paren_str[index]

		if paren in "[{(":
			# opening bracket
			stack.push(paren)
		else:
			# closing bracket
			# Edge case
			if stack.is_empty():
				is_balanced = False
				break
			else:
				top = stack.pop()
				if not is_valid_pair(opening=top, closing=paren):
					# bracket doen't match
					is_balanced = False
					break
		index += 1

	if stack.is_empty() and is_balanced:
		return True
	else: 
		return False


if __name__ == "__main__":
	pass