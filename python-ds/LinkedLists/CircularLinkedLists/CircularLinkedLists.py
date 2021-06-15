class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None


    def append(self, data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else:
            new_node = Node(data)
            current_node = self.head

            while current_node.next != self.head:
                current_node = current_node.next

            current_node.next =  new_node
            new_node.next = self.head


    def prepend(self, data):
        new_node = Node(data)
        current_node = self.head
        new_node.next = self.head

        if not self.head:
            new_node.next = new_node
        else:
            while current_node.next != self.head:
                current_node = current_node.next
            current_node.next = new_node

        self.head = new_node

    def print_list(self):
        current_node = self.head

        while current_node:
            print(current_node.data)
            current_node = current_node.next
            if current_node == self.head:
                break