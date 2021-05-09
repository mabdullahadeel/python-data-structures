from stack import Stack

"""
This functin takes a number an returns
the binary equivalance for that number.

Exceptin: Throws error if the a valid
		  number is not provided
"""


def convert_to_binary(number):
	if type(number) != int : 
		raise TypeError(f"Expected a number but found {type(number)}")

	stack = Stack()

	remiander = number

	while remiander >= 1:
		stack.push(remiander % 2)
		remiander = remiander // 2

	result = ""
	while not stack.is_empty():
		result += str(stack.pop())

	return int(result)


if __name__ == "__main__":
	# Test
	test_int = 60  # Expected Output: 111100
	result = convert_to_binary(60)
	print(result)