"""
Linked List vs Arrays:
	Linked List						Arrays
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


	def delete_node(self, key):
		current_node = self.head

		if current_node and current_node.data == key:	# Node to be deleted is the head
			self.head = current_node.next
			current_node = None
			return

		prev = None
		while current_node and current_node.data != key:
			prev = current_node
			current_node = current_node.next

		if current_node is None:
			raise Exception(f"COULD NOT FIND THE NODE TO DELETE AT {key}")

		prev.next = current_node.next
		current_node = None


	def delete_node_at_position(self, position):
		if self.head is None: return

		current_node = self.head
		if position == 0:  		# Node to delete is at the haed position
			self.head = current_node.next
			current_node = None
			return

		prev_node = None
		count = 0
		while current_node and count != position:
			prev_node = current_node
			current_node = prev.next
			count += 1

		if current_node is None:
			raise Exception(f"COULD NOT FIND THE ITEM TO DELETE AT {position}")

		prev_node.next = current_node.next
		current_node = None


if __name__ == "__main__":
	llist = SinglyLinkedList()
	llist.append("A")
	llist.append("B")
	llist.append("C")
	llist.append("D")

	llist.delete_node_at_position(0)
	llist.delete_node("B")
	# llist.delete_node("E") # % line that will raise exception %

	llist.print_list()
