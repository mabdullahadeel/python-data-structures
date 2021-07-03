from .CircularLinkedLists import CircularLinkedList


def is_circular_linked_list(input_list):
    if isinstance(input_list, CircularLinkedList):
        if input_list.head:
            current_node = input_list.head
            while current_node.next:
                current_node = current_node.next
                if current_node.next == input_list.head:
                    return True
            return False
        else:
            return False
    else:
        raise ValueError("INVALID INSTANCE")