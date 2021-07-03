"""
    Binary Search Tree provides significant
    improvement is time complexities but only
    in case of non-linear BST. For instance,

    Given are the cases 👇

    Algo                Average Case                Worst Case
    Search                O(logn)                      O(n)
    Insert                O(logn)                      O(n)
    Delete                O(logn)                      O(n)

"""


class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST(object):
    def __init__(self, root):
        self.root = Node(root)


    def insert(self, new_data):
        """
            Inserting the data to the proper node in BST
        """
        self._insert(current=self.root, new_data=new_data)


    def _insert(self, current, new_data):
        if current.data < new_data:     # new_data should be placed in right sub-tree
            if current.right:           # see if further has right subtree
                self._insert(current=current.right, new_data=new_data)
            else:
                current.right = Node(data=new_data)
        else:       # new_data should be placed in the left sub-tree
            if current.left:
                self._insert(current=current.left, new_data=new_data)
            else:
                current.left = Node(data=new_data)


    def search(self, to_find):
        """
            Determine the presence of the number in BST
            return_type -> boolean
        """
        return self._search(current=self.root, to_find=to_find)


    def _search(self, current, to_find):
        if current:
            if current.data == to_find:
                return True
            elif current.data < to_find:
                return self._search(current=current.right, to_find=to_find)
            else:
                return self._search(current=current.left, to_find=to_find)
        else:
            return False


    def delete(self, to_delete):
        """
            Delete the node with given data and rearrange the tree
        """
        self._delete(current=self.root, to_delete=to_delete)


    def _delete(self, current, to_delete):
        if current is None:     # Base case
            return current

        if current.data < to_delete:
            # the node to delete lies in the right subtree
            current.right = self._delete(current=current.right, to_delete=to_delete)
        if current.data > to_delete:
            # node to delete lies in the left sub-tree
            current.left = self._delete(current=current.left, to_delete=to_delete)
        else:       # the current node is the node to delete
            # node with only one child or no child
            if current.right is None:
                temp = current.left
                current = None
                return temp
            elif current.left is None:
                temp = current.right
                current = None
                return temp

            # CASE: Deleting the node which has both the children
            # -> inorder successor
            '''Then before deleting the node, find the smallest in its right subtree and 
            replace the node data with that to satisfy the BST properties.'''
            # 1 - Finding the smallest node in the right subtree -> inorder successor
            temp = self.min_sub_tree_val(sub_tree_root=root.right)
            # 2 - Copy the inorder successor to content to the current node which is node going to be deleted
            current.data = temp.data
            # 3 - Deleting the inorder successor since these is now duplicate of it down in the right subtree
            # and always will be leaf node
            current.right = self._delete(current=current.right, to_delete=temp.data)

        return current

    @static
    def min_sub_tree_val(self, sub_tree_root):
        current_node = sub_tree_root
        # loop down to find the left most which will be the minimum
        while current_node.left is not None:
            current_node = current_node.left

        return current_node


