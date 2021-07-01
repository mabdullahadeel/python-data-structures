from .helper_queue import Queue

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
                - levelorder
        """
        supported_types =["preorder", "inorder", "postorder", "levelorder"]
        if traversal_type not in supported_types:
            raise ValueError(f"Traversal Type {traversal_type} is not supported. ")
        if traversal_type == supported_types[0]:
            return self.preorder(start=tree.root, traversal="")
        elif traversal_type == supported_types[1]:
            return self.inorder(start=tree.root, traversal="")
        elif traversal_type == supported_types[2]:
            return self.postorder(start=tree.root, traversal="")
        elif traversal_type == supported_types[3]:
            return self.level_order_traversal(start=tree.root)


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


    def level_order_traversal(self, start):
        """
            This type of traversal uses Queue to store data while operation
            to get the desired result
        """
        if start is None:
            raise ValueError("start node not specified.")

        queue = Queue()
        queue.enqueue(start)

        traversal = ""

        while len(queue) > 0:
            traversal += str(queue.peek()) + "-"
            node = queue.dequeue()

            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

        return traversal

