from ..SinglyLinkedList import SinglyLinkedList
import pytest

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


    def test_legth(self):
        llist = HelpTestSinglyLinkedList()
        test_samples = [True, 1, "A", "B", 2, "C"]
        for i in test_samples:
            llist.append(i)

        assert llist.length() == len(test_samples)


    def test_length_recursive(self):
        llist = HelpTestSinglyLinkedList()
        test_samples = [True, 1, "A", "B", 2, "C"]
        for i in test_samples:
            llist.append(i)

        assert llist.len_recursive(llist.head) == len(test_samples)


    def test_node_swap(self):
        llist = HelpTestSinglyLinkedList()
        test_samples = ["A", "B", "D", "C"]
        for i in test_samples:
            llist.append(i)

        # Testing the error case
        with pytest.raises(ValueError):
            llist.swap_nodes("B", "B")

        # Base Case
        expected_output = ["A", "B", "C", "D"]
        llist.swap_nodes("D", "C")
        assert llist.get_linked_list_as_list() == expected_output

        # head case
        expected_output_head_node = ["B", "A", "C", "D"]
        llist.swap_nodes("A", "B")
        assert llist.get_linked_list_as_list() == expected_output_head_node


    def test_reverse_list_iterative(self):
        llist = HelpTestSinglyLinkedList()
        test_samples = [1, 2, 3]

        for i in test_samples:
            llist.append(i)
        llist.reverse_list_iterative()
        assert llist.get_linked_list_as_list() == test_samples[::-1]


    def test_reverse_list_recursive(self):
        llist = HelpTestSinglyLinkedList()
        test_samples = [1, 2, 3]

        for i in test_samples:
            llist.append(i)

        llist.reverse_recursive()

        assert llist.get_linked_list_as_list() == test_samples[::-1]


    def test_merge_sort(self):
        llist_1 = HelpTestSinglyLinkedList()
        llist_2 = HelpTestSinglyLinkedList()

        test_sample_1 = [1, 5, 7, 9, 10]
        for i in test_sample_1:
            llist_1.append(i)

        test_sample_2 = [2, 3, 4, 6, 8]
        for j in test_sample_2:
            llist_2.append(j)

        llist_1.merge_sorted(llist_2)
        expected_list = test_sample_1 + test_sample_2
        expected_list.sort()
        assert llist_1.get_linked_list_as_list() == expected_list


    def test_remove_duplicates(self):
        llist = HelpTestSinglyLinkedList()
        test_samples = [1, 2, 3, 2, 3]

        for i in test_samples:
            llist.append(i)

        llist.remove_duplicates()
        expected_output = list(set(test_samples))

        assert llist.get_linked_list_as_list() == expected_output


    def test_get_nth_from_last(self):
        llist = HelpTestSinglyLinkedList()
        test_sample = [1, 2, 3, 4]

        for i in test_sample:
            llist.append(i)

        # Testing error handling
        with pytest.raises(ValueError):
            llist.get_nth_from_last(len(test_sample) + 1)

        # Testing negative integers
        with pytest.raises(ValueError):
            llist.get_nth_from_last(-1)


