from ..DoublyLinkedList import DoublyLinkedList


class HelperTestDoublyLinkedList(DoublyLinkedList):
    """
        A wrapper class around the main 'DoublyLinkedList' class
        to provide extra functionality for testing purpose.
    """


    def __init__(self):
        super().__init__()


    def get_doubly_linked_list_as_array(self):
        results = []
        current_node = self.head

        while current_node:
            results.append(current_node.data)
            current_node = current_node.next

        return results


class TestDoublyLinkedList:

    def test_append(self):
        dllist = HelperTestDoublyLinkedList()
        test_samples = ["A", "B", "C"]

        for i in test_samples:
            dllist.append(i)

        assert dllist.get_doubly_linked_list_as_array() == test_samples


    def test_prepend(self):
        dllist = HelperTestDoublyLinkedList()
        test_samples = ["B", "C", "D"]
        test_output = ["A"] + test_samples

        for i in test_samples:
            dllist.append(i)
        dllist.prepend("A")
        assert dllist.get_doubly_linked_list_as_array() == test_output
