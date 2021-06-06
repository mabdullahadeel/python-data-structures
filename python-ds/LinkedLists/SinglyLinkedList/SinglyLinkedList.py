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


	def remove_duplicates(self):
		"""
			Remove nodes with duplicated data keeping one of a kind
			To keep track, Hask map has been used here
		"""
		current_node = self.head
		prev_node = None
		duplicate_vals = dict()

		while current_node:
			if current_node.data in duplicate_vals:
				# Delete the node
				prev_node.next =   current_node.next
				current_node = None
			else:
				duplicate_vals[current_node.data] = 1
				prev_node = current_node
			current_node = prev_node.next


	def get_nth_from_last(self, n):
		"""
			Returns the data of nth node from the last of the Linked List
		"""
		total_length = self.length()

		if n > total_length:
			raise Exception(f"{n} CANNOT BE GREATER THAN THE LENGTH OF LINKED LIST")

		if n < 0:
			raise Exception("NEGATIVE INTEGERS ARE NOT ALLOWED")			

		current_node = self.head
		while current_node:
			if total_length == n:
				return current_node.data
			total_length -= 1
			current_node = current_node.next

		if current_node is None:
			return None


	def get_occurance_iterative(self, data):
		current_node = self.head
		count = 0
		
		while current_node:
			if current_node.data == data:
				count += 1

			current_node = current_node.next

		return count


	def get_occurance_recursive(self, node, data):
		if not node:
			return 0

		if node.data == data:
			return 1 + self.get_occurance_recursive(node.next, data)
		else:
			return self.get_occurance_recursive(node.next, data)


	def rotate(self, pivot):
		"""
			Rotates the linked list around a given pivot<int> representing the position
		"""
		if self.head and self.head.next:
			pointerP = pointerQ = self.head
			prev = None
			count = 0

			while pointerP and count < pivot:  # getting the ref to 'pivot' node
				prev = pointerP
				pointerP = pointerP.next
				pointerQ = pointerQ.next
				count += 1
			pointerP = prev

			while pointerQ:
				prev = pointerQ
				pointerQ = pointerQ.next
			pointerQ = prev

			pointerQ.next = self.head
			self.head = pointerP.next
			pointerP.next = None

		else: return None


	def list_is_palindrome(self, method):
		"""
			This method checks if the current state of the linked list is palindrome
			method: there are three methods implemented, so pass argument between 1 - 3
		"""
		if method < 1 or method > 2:
			raise Exception("arg 'method' should be between 1 and 2")

		if method == 1:
			# Using python's string funcs to get desired output
			s_string = ""
			node = self.head
			while node:
				s_string += node.data
				node = node.next

			return s_string == s_string[::-1]
		
		elif method == 2:
			# Using Lists -- Stack can also be used here
			saved_res = []
			node = self.head

			while node:
				saved_res.append(node.data)
				node = node.next

			node = self.head

			while node:
				data = saved_res.pop()
				if data != node.data:
					return False
				node = node.next

			return True


		def move_tail_to_head(self):
	        if self.head and self.head.next:
	            last_node = self.head
	            to_be_last_node = None

	            while last_node.next:
	                to_be_last_node = last_node
	                last_node = last_node.next

	            last_node.next = self.head
	            to_be_last_node.next = None
	            self.head = last_node


       	def sum_two_lists(self, other_list):
			if not isinstance(other_list, SinglyLinkedList):
				raise Exception("INVALID LIST PROVIDED")

			pointerP = self.head
			pointerQ = other_list.head

			sum_list = SinglyLinkedList()
			carry = 0

			while pointerP or pointerQ:
				if not pointerP:
					p_data = 0
				else:
					p_data = pointerP.data

				if not pointerQ:
					q_data = 0
				else:
					q_data = pointerQ.data

				c_sum = p_data + q_data + carry

				if c_sum >= 10:
					carry = 1
					remainder = c_sum % 10
					sum_list.append(remainder)
				else:
					carry = 0
					sum_list.append(c_sum)

				if pointerP:
					pointerP = pointerP.next
				if pointerQ:
					pointerQ = pointerQ.next
			return sum_list



if __name__ == "__main__":
	pass

