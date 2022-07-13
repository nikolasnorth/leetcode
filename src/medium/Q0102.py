"""
102. Binary Tree Level Order Traversal
https://leetcode.com/problems/binary-tree-level-order-traversal/
"""
from __future__ import annotations
from dataclasses import dataclass


@dataclass
class TreeNode:
    val: int
    left: TreeNode
    right: TreeNode


# Time: O(n), Space: O(n), where n is the number of nodes in the Binary Tree.
def level_order(root: TreeNode | None) -> list[list[int]]:
    if not root:
        return []
    res: list[list[int]] = []
    tmp: list[TreeNode] = [root]
    while len(tmp) > 0:
        tmp_vals = [node.val for node in tmp]
        res.append(tmp_vals)
        new_tmp: list[TreeNode] = []
        for node in tmp:
            if node.left:
                new_tmp.append(node.left)
            if node.right:
                new_tmp.append(node.right)
        tmp = new_tmp
    return res
