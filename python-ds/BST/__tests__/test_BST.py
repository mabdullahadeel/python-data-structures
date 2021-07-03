from ..BST import BST


class HelpTestBST(BST):
    """
        A utility class to enhance the functionality of base
        class for testing purpose
    """
    def __init__(self, root):
        super(HelpTestBST, self).__init__(root=root)

    def _inorder(self, start, traversal=""):
        """ Left -> Root -> Right """
        if start:
            traversal = self._inorder(start=start.left, traversal=traversal)
            traversal += (str(start.data) + "-")
            traversal = self._inorder(start=start.right, traversal=traversal)

        return traversal


def test_bst_search():
    bst = HelpTestBST(10)
    bst.insert(3)
    bst.insert(1)
    bst.insert(25)
    bst.insert(9)
    bst.insert(13)

    assert bst.search(9) # -> Should return `True`
    assert not bst.search(41) # -> Should return `False`


def test_bst_insertion():
    bst = HelpTestBST(10)
    bst.insert(3)
    bst.insert(1)
    bst.insert(25)
    bst.insert(9)
    bst.insert(13)

    assert bst.search(9) # -> Should return `True`


def test_bst_delete():
    #          50
    #       /     \
    #      30      70
    #     /  \    /  \
    #   20   40  60   80

    bst = HelpTestBST(50)
    bst.insert(30)
    bst.insert(20)
    bst.insert(40)
    bst.insert(70)
    bst.insert(60)
    bst.insert(80)

    bst.delete(to_delete=20)
    assert bst._inorder(start=bst.root) == "30-40-50-60-70-80-"

    bst.delete(to_delete=30)
    assert bst._inorder(start=bst.root) == "40-50-60-70-80-"

    bst.delete(to_delete=50)
    assert bst._inorder(start=bst.root) == "40-60-70-80-"
