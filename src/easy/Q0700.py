"""
700. Search in a Binary Search Tree
https://leetcode.com/problems/search-in-a-binary-search-tree/
"""

from __future__ import annotations
from dataclasses import dataclass


@dataclass
class TreeNode:
    val: int = 0
    left: TreeNode | None = None
    right: TreeNode | None = None


# Time: O(n), Space: O(log n), where n is the number of nodes in the binary tree
def search_bst(root: TreeNode | None, val: int) -> TreeNode | None:
    if root is None:
        return None
    if root.val == val:
        return root
    return search_bst(root=root.left, val=val) or search_bst(root=root.right, val=val)
