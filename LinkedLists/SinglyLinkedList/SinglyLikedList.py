"""
Linked List vs Arrays:
	Lineked List						Arrays
	Insertion at index 0: O(1)			Insertionat index 0: O(n)
	Deletion at index 0: O(1)			Deletion at index 0: O(n)
	Access Element: O(n)				Access Element: O(1)
	Contiguous Memory: NO				Contiguous Memory: YES
"""


class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


class SinglyLinkedList:
	def __init__(self):
		self.head = None


	def append(self, data):
		""" 
			Appending Data at the end of the linked List
		"""
		new_node = Node(data)
		if self.head is None:  		# In case of empty Linked List
			self.head = new_node
			return

		last_node = self.head		# Non-Empty Linked List
		while last_node.next:
			last_node = last_node.next

		last_node.next = new_node


	def print_list(self):
		"""
			prints data available the linked list to console
		"""
		current_node = self.head

		while current_node:
			print(current_node.data)
			current_node = current_node.next


	def prepend(self, data):
		"""
			Insert the data at the beginning of the linked list
		"""
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node


	def insert_after_node(self, prev_node, data):
		if not prev_node:
			raise Exception("NO NODE FOUND TO INSERT AFTER")

		new_node = Node(data)
		new_node.next = prev_node.next
		prev_node.next = new_node


if __name__ == "__main__":
	llist = SinglyLinkedList()
	llist.append("A")
	llist.append("B")
	llist.append("C")
	llist.insert_after_node(llist.head, "D")
	llist.print_list()