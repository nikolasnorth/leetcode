"""
230. Kth Smallest Element in a BST
https://leetcode.com/problems/kth-smallest-element-in-a-bst/
"""
from __future__ import annotations
from dataclasses import dataclass


@dataclass
class TreeNode:
    val: int
    left: TreeNode | None
    right: TreeNode | None


# Time: O(k) if k > log n, otherwise O(log n), where n is the number of nodes in the tree.
# Space: O(k)
def kth_smallest(root: TreeNode | None, k: int) -> int:
    vals = []

    def dfs(node: TreeNode | None) -> None:
        if node is None:
            return
        dfs(node.left)
        if len(vals) < k:
            vals.append(node.val)
        if len(vals) < k:
            dfs(node.right)

    dfs(root)
    return vals[-1]
