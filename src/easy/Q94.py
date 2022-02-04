"""
94. Binary Tree Inorder Traversal
https://leetcode.com/problems/binary-tree-inorder-traversal/
"""
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Recursive solution
# O(n) time, O(log n) space, where n is the number of nodes in the tree
def inorder_traversal_1(root: Optional[TreeNode]):
    if not root:
        return []
    return inorder_traversal_1(root.left) + [root.val] + inorder_traversal_1(root.right)


# Iterative solution
# O(n) time, O(n) space, where n is the number of nodes in the tree
def inorder_traversal_2(root: Optional[TreeNode]):
    result: List[int] = []
    stack: List[TreeNode] = []
    current = root
    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        top = stack.pop()
        result.append(top.val)
        current = top.right
    return result
