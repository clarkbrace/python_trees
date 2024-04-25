from typing import List


class BinaryTreeNode:
    def __init__(self, val: int = None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, value: int):
        self.root = None
        self.root = BinaryTreeNode(value)

    def __init__(self, nodes: List[int]):
        self.root = None
        for node in nodes:
            self.insert(node)

    def __str__(self):
        return self.create_f_string(self.root)

    def __contains__(self, item: int):
        return self.binary_search(self.root, item)

    def create_f_string(self, root):
        if not root:
            return "None"
        return f"(V: {root.val} | L: {self.create_f_string(root.left)} | R: {self.create_f_string(root.right)})"

    def inserts(self, values: [int]):
        for value in values:
            self.insert(value)

    def insert(self, value: int):

        if not self.root:
            self.root = BinaryTreeNode(value)
            return

        current_node = self.root
        prev = self.root

        while current_node:
            prev = current_node

            if current_node.val == value:
                break

            if value < current_node.val:
                current_node = current_node.left
            else:
                current_node = current_node.right

        # Add node to tree
        if value < prev.val:
            prev.left = BinaryTreeNode(value)
        elif value > prev.val:
            prev.right = BinaryTreeNode(value)

    def binary_search(self, node: BinaryTreeNode, target: int):

        if not node:
            return False

        if node.val == target:
            return True
        if target < node.val:
            return self.binary_search(node.left, target)
        else:
            return self.binary_search(node.right, target)

    def remove(self, target):
        # Find Node to be removed
        current_node = self.root
        prev_node = current_node

        while current_node:

            if current_node.val == target:
                break

            prev_node = current_node

            if target < current_node.val:
                current_node = current_node.left
            else:
                current_node = current_node.right

        # If node is not present
        if not current_node:
            return None

            # If node is present
        # Removed node has no children
        if target < prev_node.val:
            rm_val = prev_node.left.val
            prev_node.left = None
            return rm_val
        else:
            rm_val = prev_node.left.val
            prev_node.left = None
            return rm_val

        # Preform removal operations
