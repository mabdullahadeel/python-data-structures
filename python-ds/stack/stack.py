"""
Stack data structure is way of
storing | organizing data in the
form of stacks. These stacks are
books stack i-e piling books on
top of each other
"""

class Stack:
	"""
		The stack implemented in this
		class uses reverse list operations
		provided by python built-in 'list' class
		i-e The last element in the list
		is the top element of the stack
	"""
	def __init__(self):
		self.items = []


	def push(self, item):
		"""Add to the end of the list -> Top in stack"""
		self.items.append(item)


	def pop(self):
		"""Remove the last element from the list -> Top from stack"""
		return self.items.pop()


	def is_empty(self):
		return len(self.items) == 0


	def peek(self):
		"""
			Returns the last inserted item in the stack i-e
			the item at the top of the stack
		"""
		if not self.is_empty():
			return self.items[-1]
		else:
			return None


	def get_stack(self):
		return self.items
