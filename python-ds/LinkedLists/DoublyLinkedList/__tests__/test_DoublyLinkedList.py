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


    def test_insert_after_node(self):
        dllist = HelperTestDoublyLinkedList()
        test_samples = ["A", "C", "D"]
        test_output = ["A", "B", "C", "D", "E"]

        for i in test_samples:
            dllist.append(i)

        # inserting in the middle -> inserting "B" after "A"
        dllist.insert_after_node(key="A", data="B")
        # inserting at the end of the list -> inserting "E" after "D"
        dllist.insert_after_node(key="D", data="E")

        assert dllist.get_doubly_linked_list_as_array() == test_output


    def test_insert_node_before(self):
        dllist = HelperTestDoublyLinkedList()
        test_samples = ["B", "D", "E"]
        test_output = ["A", "B", "C", "D", "E"]

        for i in test_samples:
            dllist.append(i)

        # inserting at the start -> inserting  "A" before "B"
        dllist.insert_node_before(key="B", data="A")
        # inserting in the middle before the given node -> inserting "C" before "D"
        dllist.insert_node_before(key="D", data="C")

        assert dllist.get_doubly_linked_list_as_array() == test_output


    def test_delete_node(self):
        # testing the case I
        dllist_c1 = HelperTestDoublyLinkedList()
        test_samples_c1 = ["A"]

        for i in test_samples_c1:
            dllist_c1.append(i)

        dllist_c1.delete_node(key="A")
        assert dllist_c1.get_doubly_linked_list_as_array() == []

        # testing case 2
        dllist_c2 = HelperTestDoublyLinkedList()
        test_samples_c2 = ["A", "B"]

        for i in test_samples_c2:
            dllist_c2.append(i)

        dllist_c2.delete_node(key="A")
        assert dllist_c2.get_doubly_linked_list_as_array() == [test_samples_c2[-1]]

        # testing case 3
        dllist_c3 = HelperTestDoublyLinkedList()
        test_samples_c3 = ["A", "B", "C"]
        test_output_c3 = ["A", "C"]

        for i in test_samples_c3:
            dllist_c3.append(i)

        dllist_c3.delete_node(key="B")
        assert dllist_c3.get_doubly_linked_list_as_array() == test_output_c3

        # testing case 4
        dllist_c4 = HelperTestDoublyLinkedList()
        test_samples_c4 = ["A", "B", "C"]

        for i in test_samples_c4:
            dllist_c4.append(i)

        dllist_c4.delete_node(key="C")
        assert dllist_c4.get_doubly_linked_list_as_array() == test_samples_c4[0:2]


    def test_reverse(self):
        dllist = HelperTestDoublyLinkedList()
        test_sample = ["A", "B", "C"]

        for i in test_sample:
            dllist.append(i)

        dllist.reverse()

        assert dllist.get_doubly_linked_list_as_array() == test_sample[::-1]


