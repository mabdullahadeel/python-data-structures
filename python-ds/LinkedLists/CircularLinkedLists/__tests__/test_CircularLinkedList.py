from ..CircularLinkedLists import CircularLinkedList

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