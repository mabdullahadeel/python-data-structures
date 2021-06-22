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
