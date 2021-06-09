from ..stack import Stack


class StackTestClass(Stack):
	"""
		A helper calss wrapped around the main
		'Stack' class to provide additional 
		functionality for testing purpose
	"""

	def __init__(self):
		super().__init__()



class TestStack:
	""" Actual Test Class """


	def test_get_stack(self):
		stack = StackTestClass()
		test_list = ["A", "B", "C", 1, 2, 3, True]

		for i in test_list:
			stack.push(i)

		assert stack.get_stack() == test_list


	def test_push(self):
		stack = StackTestClass()

		test_list = ["A", "B", "C"]
		for i in test_list:
			stack.push(i)

		assert stack.get_stack() == test_list


	def test_pop(self):
		stack = StackTestClass()

		test_list = [1, 2, 3, 4, 5]
		for i in test_list:
			stack.push(i)

		number_of_popping = 2
		# removing top `number_of_popping` items
		if number_of_popping <= len(stack.get_stack()):
			for i in range(number_of_popping):
				stack.pop()
			assert stack.get_stack() == test_list[:len(test_list) - number_of_popping]
		else:
			raise Exception(
				"Cannot pop elements more than length"
				)


	def test_is_empty(self):
		stack = StackTestClass()
		test_list = ["A", "B", "C", 1, 2, 3]

		# adding all
		for i in test_list:
			stack.push(i)

		# removing all 
		for _i in range(len(test_list)):
			stack.pop()

		assert stack.is_empty() == True


	def test_peek(self):
		stack = StackTestClass()
		test_list = ["A", "B", "C", 1, 2, 3, True]

		for i in test_list:
			stack.push(i)

		assert stack.peek() == test_list[-1]


