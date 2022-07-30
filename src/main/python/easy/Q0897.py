"""
897. Increasing Order Search Tree
https://leetcode.com/problems/increasing-order-search-tree/
"""

from __future__ import annotations
from dataclasses import dataclass


@dataclass
class TreeNode:
    val: int = 0
    left: TreeNode | None = None
    right: TreeNode | None = None


# Time: O(n), Space: O(n), where n is the number of nodes in the tree.
def increasing_bst(root: TreeNode) -> TreeNode:
    vals = []

    def dfs(node: TreeNode | None) -> None:
        if node is None:
            return
        dfs(node.left)
        vals.append(node.val)
        dfs(node.right)

    dfs(root)
    dummy = current = TreeNode()
    for val in vals:
        current.right = TreeNode(val)
        current = current.right
    return dummy.right
