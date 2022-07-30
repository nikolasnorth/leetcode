"""
669. Trim a Binary Search Tree
https://leetcode.com/problems/trim-a-binary-search-tree/
"""
from __future__ import annotations
from dataclasses import dataclass


@dataclass
class TreeNode:
    val: int
    left: TreeNode | None
    right: TreeNode | None


# Time: O(n), Space: O(log n), where n is the number of nodes in the tree.
def trim_bst(root: TreeNode | None, low: int, high: int) -> TreeNode | None:
    if root is None:
        return None
    if root.val < low:
        return trim_bst(root.right, low, high)
    if root.val > high:
        return trim_bst(root.left, low, high)
    root.left = trim_bst(root.left, low, high)
    root.right = trim_bst(root.right, low, high)
    return root
