from stack import Stack

"""
This functin takes a string and returns
the reverse of that string using Stack

edge case: If a number is given to the 
function, it will treat it as string.
"""


def reverse_string(string):
	stack = Stack()

	for alphabet in str(string):
		stack.push(alphabet)

	reversed_str = ""

	while not stack.is_empty():
		reversed_str += stack.pop()

	return reversed_str


# Test
test_str = "Hello Stack"
res = reverse_string(test_str)
print(res)