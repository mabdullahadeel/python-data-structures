class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(value=root)


    def get_binary_tree(self, traversal_type, tree):
        """
            A helper method that takes 'traversal_type: str' as
            argument and call the respective function and return
            the result as per the traversal_type passed
            SUPPORTED TYPES:
                - preorder
                - inorder
                - postorder
        """
        supported_types =["preorder", "inorder", "postorder"]
        if traversal_type not in supported_types:
            raise ValueError(f"Traversal Type {traversal_type} is not supported. ")
        if traversal_type == supported_types[0]:
            return self.preorder(start=tree.root, traversal="")
        elif traversal_type == supported_types[1]:
            return self.inorder(start=tree.root, traversal="")
        else:
            return self.postorder(start=tree.root, traversal="")


    def preorder(self, start, traversal):
        """ Root -> Left -> Right """
        if start:
            traversal += (str(start.value) + '-')
            traversal = self.preorder(start=start.left, traversal=traversal)
            traversal = self.preorder(start=start.right, traversal=traversal)

        return traversal


    def inorder(self, start, traversal):
        """ Left -> Root -> Right """
        if start:
            traversal = self.inorder(start=start.left, traversal=traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder(start=start.right, traversal=traversal)

        return traversal


    def postorder(self, start, traversal):
        """ Left -> Right -> Root """
        if start:
            traversal = self.postorder(start=start.left, traversal=traversal)
            traversal = self.postorder(start=start.right, traversal=traversal)
            traversal += (str(start.value) + "-")

        return traversal
