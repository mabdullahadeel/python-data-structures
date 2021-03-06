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


def test_level_order_traversal():
    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)

    assert tree.get_binary_tree(traversal_type="levelorder", tree=tree) == "1-2-3-4-5-"


def test_reverse_level_order_traversal():
    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)

    assert tree.get_binary_tree(traversal_type="reverse_levelorder", tree=tree) == "4-5-2-3-1-"


def test_height_bn():
    # Calculate height of binary tree:
    #     1
    #    / \
    #   2  3
    #  / \
    # 4  5
    #
    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)

    assert tree.height(node=tree.root) == 2


def test_size():
    # Calculate SIZE of binary tree: ==> 5 since there are total 5 nodes
    #     1
    #    / \
    #   2  3
    #  / \
    # 4  5
    #
    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)

    assert tree.size(node=tree.root) == 5