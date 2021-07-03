class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None


    def __len__(self):
        current_node = self.head
        count = 0

        while current_node:
            count += 1
            current_node = current_node.next
            if current_node == self.head:
                break

        return count


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


    def remove_node_by_data(self, key):
        """
            Removing the node from the circular linked list
            Assumptions: There is no duplicate node -> the node
            to be removed is occurring once
        """
        if self.head:
            if self.head.data == key:        # node to delete is head
                last_node = self.head

                while last_node.next != self.head:
                    last_node = last_node.next

                if self.head == self.head.next:     # head is the only element in the list
                    self.head = None
                else:
                    last_node.next = self.head.next
                    self.head = self.head.next
            else:
                current_node = self.head
                prev_node = None

                while current_node.next != self.head:
                    prev_node = current_node
                    current_node = current_node.next

                    if current_node.data == key:
                        prev_node.next = current_node.next
                        current_node = current_node.next
        else:
            raise ValueError(
                "CANNOT REMOVE NODE FROM EMPTY CIRCULAR LINKED LIST"
            )


    def split_list(self):
        """
            Splitting the circular linked list into two halves
        """

        size = len(self)

        if size == 0:       # Empty List
            return None
        if size == 1:       # One element in the list
            return self.head

        mid = size//2
        count = 0

        prev_node = Node
        current_node = self.head

        # Creating the first half
        while current_node and count < mid:
            count += 1
            prev_node = current_node
            current_node = current_node.next
        prev_node.next = self.head

        split_list = CircularLinkedList()
        while current_node.next != self.head:
            split_list.append(current_node.data)
            current_node = current_node.next
        split_list.append(current_node.data)

        return {
            "first_half": self,
            "second_half": split_list
        }
