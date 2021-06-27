from ..binaryTree import BinaryTree, Node
import pytest


def test_get_binary_tree_error_start():
    tree = BinaryTree(1)
    with pytest.raises(ValueError):
        tree.get_binary_tree(traversal_type="random_type", tree=tree)


def test_binary_tree():
    # 1-2-4-5-3-6-7-
    # 4-2-5-1-6-3-7
    # 4-5-2-6-7-3-1
    #               1
    #           /       \
    #          2          3
    #         /  \      /   \
    #        4    5     6   7

    # Set up tree:
    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)

    assert tree.get_binary_tree(traversal_type="preorder", tree=tree) == "1-2-4-5-3-6-7-"
    assert tree.get_binary_tree(traversal_type="inorder", tree=tree) == "4-2-5-1-6-3-7-"
    assert tree.get_binary_tree(traversal_type="postorder", tree=tree) == "4-5-2-6-7-3-1-"
