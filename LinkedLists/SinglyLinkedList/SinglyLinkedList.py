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


	def length(self):
		current_node = self.head
		count = 0
		while current_node:
			current_node = current_node.next
			count += 1

		return count

	def len_recursive(self, node):
		if node is None:
		    return 0
		return 1 + self.len_recursive(node.next)


	def swap_nodes(self, key1, key2):
		if key1 == key2:
			raise Exception("GIVEN NODES MUST BE DIFFERENT TO BE SWAPPED")

		prev_node_1 = None
		current_node_1 = self.head

		while current_node_1 and current_node_1.data != key1:
			prev_node_1 = current_node_1
			current_node_1 = current_node_1.next

		prev_node_2 = None
		current_node_2 = self.head

		while current_node_2 and current_node_2.data != key2:
			prev_node_2 = current_node_2
			current_node_2 = current_node_2.next


		if not current_node_1 or not current_node_2:
			raise Exception("COULD NOT FIND THE NODE TO SWAP")


		# Handling the cases of one of the nodes at the `head`
		if prev_node_1:
			prev_node_1.next = current_node_2
		else:
			self.head = current_node_2

		if prev_node_2:
			prev_node_2.next = current_node_1
		else:
			self.head = current_node_1


		current_node_1.next, current_node_2.next = current_node_2.next, current_node_1.next

	# def swap_nodes(self, key_1, key_2):

	# 	if key_1 == key_2:
	# 	    return 

	# 	prev_1 = None 
	# 	curr_1 = self.head 
	# 	while curr_1 and curr_1.data != key_1:
	# 	    prev_1 = curr_1 
	# 	    curr_1 = curr_1.next

	# 	prev_2 = None 
	# 	curr_2 = self.head 
	# 	while curr_2 and curr_2.data != key_2:
	# 	    prev_2 = curr_2 
	# 	    curr_2 = curr_2.next

	# 	if not curr_1 or not curr_2:
	# 	    return 

	# 	if prev_1:
	# 	    prev_1.next = curr_2
	# 	else:
	# 	    self.head = curr_2

	# 	if prev_2:
	# 	    prev_2.next = curr_1
	# 	else:
	# 	    self.head = curr_1

	# 	curr_1.next, curr_2.next = curr_2.next, curr_1.next

if __name__ == "__main__":
	llist = SinglyLinkedList()
	llist.append("A")
	llist.append("B")
	llist.append("C")
	llist.append("D")

	llist.swap_nodes("B", "C")
	print("Swapping nodes B and C that are not head nodes")
	llist.print_list()

