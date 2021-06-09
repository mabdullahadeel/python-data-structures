from ..SinglyLinkedList import SinglyLinkedList


class HelpTestSinglyLinkedList(SinglyLinkedList):
    """
    		A helper class wrapped around the main
    		'Stack' class to provide additional
    		functionality for testing purpose
    """


    def __init__(self):
        super().__init__()


    def get_linked_list_as_list(self):
        results = []
        current_node = self.head
        while current_node:
            results.append(current_node.data)
            current_node = current_node.next
        return  results



class TestSinglyLinkedLists:


    def test_append(self):
        llist = HelpTestSinglyLinkedList()
        test_samples = ["A", "B", "C", "D", 1, 2]

        for i in test_samples:
            llist.append(i)

        assert llist.get_linked_list_as_list() == test_samples


    def test_prepend(self):
        llist = HelpTestSinglyLinkedList()
        test_samples = ["B", "C"]
        required_sample = ["A", "B", "C"]

        for i in test_samples:
            llist.append(i)

        llist.prepend("A")
        assert llist.get_linked_list_as_list() == required_sample


    def test_insert_after_node(self):
        llist = HelpTestSinglyLinkedList()
        test_samples = ["A", "B", "D"]
        required_sample = ["A", "B", "C", "D"]

        for i in test_samples:
            llist.append(i)

        llist.insert_after_node(llist.head.next, "C")
        assert llist.get_linked_list_as_list() == required_sample


    def test_head_node_deletion_by_value(self):
        llist = HelpTestSinglyLinkedList()
        test_samples = ["A", "B", "C", "D", 1, 2]

        for i in test_samples:
            llist.append(i)

        llist.delete_node(test_samples[0])
        assert llist.get_linked_list_as_list() == test_samples[1:]


    def test_delete_non_head_node_by_value(self):
        llist = HelpTestSinglyLinkedList()
        test_samples = ["A", "B", "C", "D", 1, 2]

        for i in test_samples:
            llist.append(i)

        llist.delete_node(test_samples[3])    # D
        assert llist.get_linked_list_as_list() == [j for j in test_samples if j != test_samples[3]]


    def test_delete_node_at_position(self):
        # CASE I: deleting head/first node
        llist = HelpTestSinglyLinkedList()
        test_samples = ["A", "B", "C", "D", 1, 2]
        for i in test_samples:
            llist.append(i)
        llist.delete_node_at_position(0)
        passed_head_deletion = llist.get_linked_list_as_list() == test_samples[1:]

        # CASE II: deleting node from the middle
        llist = HelpTestSinglyLinkedList()
        test_samples = ["A", "B", "C", "D", 1, 2]
        for i in test_samples:
            llist.append(i)
        position = 2
        llist.delete_node_at_position(2)
        resulted_sample = test_samples
        resulted_sample.pop(position)
        passed_body_deletion = llist.get_linked_list_as_list() == resulted_sample

        assert passed_head_deletion and passed_body_deletion
