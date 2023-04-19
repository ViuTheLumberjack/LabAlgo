import random

class Node:
    def __init__(self, key, parent=None, left=None, right=None):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right

class ABR:
    def __init__(self):
        self.root = None
        self.length = 0

    def inorder_tree_walk(self, node: Node):
        if node is not None:
            self.inorder_tree_walk(node.left)
            print(node.key)
            self.inorder_tree_walk(node.right)

    def preorder_tree_walk(self, node: Node):
        if node is not None:
            print(node.key)
            self.preorder_tree_walk(node.left)
            self.preorder_tree_walk(node.right)

    def postorder_tree_walk(self, node: Node):
        if node is not None:
            self.postorder_tree_walk(node.left)
            self.postorder_tree_walk(node.right)
            print(node.key)

    def search(self, x: Node, k: int) -> Node:
        if x is None or x.key == k:
            return x
        if k < x.key:
            return self.search(self, x.left, k)
        else:
            return self.search(self, x.right, k)

    def max(self):
        x = self.root
        while x is not None:
            x = x.right

        return x.key

    def min(self):
        x = self.root
        while x is not None:
            x = x.left

        return x.key

    def tree_insert(self, z: Node):
        y = None
        x = self.root
        while x is not None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right

        z.parent = y
        if y is None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

        self.length += 1