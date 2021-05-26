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


	def reverse_list_iterative(self):
		"""
			Iterative approach to reverse a linked list
		"""
		prev_node = None
		current_node = self.head

		while current_node:
			next_node = current_node.next
			current_node.next = prev_node
			prev_node = current_node
			current_node = next_node

		self.head = prev_node
		

	def reverse_recursive(self):
		"""
			Recursive Approach to reverse Singly Linked Lists
		"""

		def _reverse_recursive(current_node, prev_node):
			if not current_node:
				return prev_node

			next_node = current_node.next
			current_node.next = prev_node
			prev_node = current_node
			current_node = next_node
			return _reverse_recursive(current_node, prev_node)

		self.head = _reverse_recursive(current_node=self.head, prev_node=None)


	def merge_sorted(self, other_linked_list):
		"""
			Merging two already sorted Signly Linked Lists
			to output a final sorted merged linked List
			Assunmption:
				- Each participant list have at least one character
		"""	
		pointerP = self.head
		pointerQ = other_linked_list.head
		pointerS = None

		if not pointerP:
			return pointerQ
		if not pointerQ:
			return pointerP

		# 'pointerS' will always have a reference to the smaller of two lists
		if pointerP and pointerQ:
			if pointerP.data <= pointerQ.data:
				pointerS = pointerP
				pointerP = pointerS.next
			else:
				pointerS = pointerQ
				pointerQ = pointerS.next
			new_head = pointerS

		while pointerP and pointerQ:
			if pointerP.data <= pointerQ.data:
				pointerS.next = pointerP
				pointerS = pointerP
				pointerP = pointerS.next
			else:
				pointerS.next = pointerQ
				pointerS = pointerQ
				pointerQ = pointerS.next

		# End of one of the list
		if not pointerP:
			pointerS.next = pointerQ
		if not pointerQ:
			pointerS.next = pointerP

		self.head = new_head
		return self.head


if __name__ == "__main__":
	pass

