from .DoublyLinkedList import DoublyLinkedList

def find_pais_with_sum(sum_value: int, doubly_linked_list: DoublyLinkedList):
    """
        This function uses Linked list to find all the possible
        pairs in the linked list that sums to the given number
    """
    pairs = list()
    head = doubly_linked_list.head
    next_node = None

    while head:
        next_node = head.next
        while next_node:
            if (head.data + next_node.data)  == sum_value:
                pairs.append(f"({str(head.data)},{str(next_node.data)})")
            next_node = next_node.next
        head = head.next

    return pairs
