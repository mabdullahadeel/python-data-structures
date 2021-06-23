class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None


    def append(self, data):
        """
            adding new element to the end of the linked list
        """
        if self.head is None:
            new_node = Node(data=data)
            self.head = new_node
        else:
            new_node = Node(data=data)
            current_node = self.head

            while current_node.next:
                current_node = current_node.next

            current_node.next = new_node
            new_node.prev = current_node


    def prepend(self, data):
        """
            adding to the beginning of the linked list.
        """
        if self.head is None:
            new_node = Node(data=data)
            self.head = new_node
        else:
            new_node = Node(data=data)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node


    def print_list(self):
        """
            Printing the list to the console.
        """
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next


    def insert_after_node(self, key, data):
        """
            create new node and add/insert that node right after
            the node with provided key
        """
        current_node = self.head
        while current_node:
            if current_node.next is None and current_node.data == key:      # case when inserting at the end of the list
                self.append(data)
                return
            elif current_node.data == key:
                new_node = Node(data=data)
                next_node = current_node.next
                current_node.next = new_node
                new_node.next = next_node
                new_node.prev = current_node
                next_node.prev = new_node
                return

            current_node = current_node.next


    def insert_node_before(self, key, data):
        """
            create new node and add/insert that node right before
            the node with provided key
        """
        current_node = self.head
        while current_node:
            if current_node.prev is None and current_node.data == key:      # case when inserting node at the beginning
                self.prepend(data=data)
                return
            elif current_node.data == key:
                new_node = Node(data=data)
                prev_node = current_node.prev
                prev_node.next = new_node
                current_node.prev = new_node
                new_node.next = current_node
                current_node.prev = prev_node
                return

            current_node = current_node.next


    def delete_node(self, key):
        """
            deleting node with provided data
            Assumptions: There is only one node with the given data i-e first node
            with the data passed to the method will be deleted. To delete two nodes
            having same data, this method needs to be called twice.

            CASES:
                CASE I: deleting the only node present in the list (list has only one node)
                CASE II: deleting head node
                CASE III: deleting node other than head where `current.next` is not `None`
                        i-e the node to be deleted is not the head node nor the last node.
                CASE IV: deleting node other than head where `current.next` is `None`
                        i-e node to be deleted is the last node of the list
        """

        current_node = self.head
        while current_node:
            if current_node.data == key and current_node == self.head:
                # CASE I
                if not current_node.next:   # making sure next node is None means the head is the only node
                    current_node = None
                    self.head = None
                    return

                # CASE 2
                else:
                    next_node = current_node.next
                    current_node.next = None
                    next_node.prev = None
                    current_node = None
                    self.head = next_node
                    return

            elif current_node.data == key:
                # CASE 3
                if current_node.next:
                    next_node = current_node.next
                    prev_node = current_node.prev

                    prev_node.next = next_node
                    next_node.prev = prev_node

                    current_node.next = None
                    current_node.prev = None
                    current_node = None
                    return

                # CASE IV
                else:
                    prev_node = current_node.prev

                    prev_node.next = None
                    current_node.prev = None
                    current_node = None
                    return

            current_node = current_node.next
