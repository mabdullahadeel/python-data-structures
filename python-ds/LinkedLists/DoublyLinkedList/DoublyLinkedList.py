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

