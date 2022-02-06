"""
100. Same Tree
https://leetcode.com/problems/same-tree/
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# O(n) time, O(log n) space, where n is the maximum number of nodes in p or q.
# Assumes p and q are ~balanced trees. If p or q are fully imbalanced then the space
# complexity is O(n).
def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]):
    if not (p or q):
        return True
    if not (p and q):
        return False
    if p.val != q.val:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)
