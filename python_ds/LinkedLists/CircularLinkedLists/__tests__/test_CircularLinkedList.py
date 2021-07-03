import pytest
from ..CircularLinkedLists import CircularLinkedList
from ..is_CircularLinkedList import is_circular_linked_list


class HelpTestCircularLinkedList(CircularLinkedList):
    """
        Helper class wrapped around the main class for testing purpose.
    """


    def __int__(self):
        super().__init__()


    def get_circular_linked_list_as_list(self):
        results = []
        current_node = self.head

        while current_node.next:
            results.append(current_node.data)
            current_node = current_node.next
            if current_node == self.head:
                break

        return results


    @staticmethod
    def get_array_from_circular_ll(circular_linked_list):
        if isinstance(circular_linked_list, CircularLinkedList):
            results = []
            current_node = circular_linked_list.head

            while current_node.next:
                results.append(current_node.data)
                current_node = current_node.next
                if current_node == circular_linked_list.head:
                    break

            return results


class TestCircularLinkedList:


    def test_append(self):
        cllist = HelpTestCircularLinkedList()
        test_sample = ["A", "B", "C", "D"]

        for i in test_sample:
            cllist.append(i)

        assert  cllist.get_circular_linked_list_as_list() == test_sample


    def test_prepend(self):
        cllist = HelpTestCircularLinkedList()
        test_samples = ["B", "C"]
        sample_output = ["A"] + test_samples

        for i in test_samples:
            cllist.append(i)

        cllist.prepend("A")

        assert cllist.get_circular_linked_list_as_list() == sample_output


    def test_remove_node_by_data(self):
        cllist = HelpTestCircularLinkedList()
        test_sample = ["A", "B", "C", "D", "E", "F"]
        sample_output = ["B", "D", "E", "F"]

        # Checking the error state
        with pytest.raises(ValueError):
            cllist.remove_node_by_data("A")

        for i in test_sample:
            cllist.append(i)
        cllist.remove_node_by_data("A")
        cllist.remove_node_by_data("C")

        assert cllist.get_circular_linked_list_as_list() == sample_output


    def test_split_list(self):
        cllist = HelpTestCircularLinkedList()
        test_sample = ["A", "B", "C", "D", "E", "F", "G"]

        for i in test_sample:
            cllist.append(i)

        split_list = cllist.split_list()

        assert (
            (cllist.get_array_from_circular_ll(split_list["first_half"]) == test_sample[0:3])
            and
            (cllist.get_array_from_circular_ll(split_list["second_half"]) == test_sample[3:])
        )


def test_is_circular_linked_list():
    cllist = HelpTestCircularLinkedList()
    test_samples = ["A", "B", "C"]

    # Testing Exception
    with pytest.raises(ValueError):
        is_circular_linked_list("random_invalid_instance")

    for i in test_samples:
        cllist.append(i)


    assert is_circular_linked_list(cllist) == True
