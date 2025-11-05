from node import Node

class BST:
    def __init__(self):
        self.root = None

    def __init__(self, value):
        self.root = Node(value)

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
            return

        current = self.root
        while True:
            if key == current.key:
                return
            elif key < current.key:
                if current.left is None:
                    current.left = Node(key)
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = Node(key)
                    return
                current = current.right

    def preorder(self):
        res = []

        def dfs(node):
            if not node:
                return
            res.append(node.key)   # node
            dfs(node.left)        # left
            dfs(node.right)       # right

        dfs(self.root)
        return res

    def postorder(self):
        res = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)        # left
            dfs(node.right)       # right
            res.append(node.key)  # node

        dfs(self.root)
        return res

    def inorder(self):
        res = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)        # left
            res.append(node.key)  # node
            dfs(node.right)       # right

        dfs(self.root)
        return res

    def reverse_preorder(self):
        res = []

        def dfs(node):
            if not node:
                return
            res.append(node.key)   # node
            dfs(node.right)        # right
            dfs(node.left)         # left

        dfs(self.root)
        return res

    def reverse_postorder(self):
        res = []

        def dfs(node):
            if not node:
                return
            dfs(node.right)        # right
            dfs(node.left)         # left
            res.append(node.key)   # node

        dfs(self.root)
        return res

    def reverse_inorder(self):
        res = []

        def dfs(node):
            if not node:
                return
            dfs(node.right)        # right
            res.append(node.key)   # node
            dfs(node.left)         # left

        dfs(self.root)
        return res