"""
99. Recover Binary Search Tree
https://leetcode.com/problems/recover-binary-search-tree/
"""
from __future__ import annotations
from dataclasses import dataclass


@dataclass
class TreeNode:
    val: int
    left: TreeNode | None
    right: TreeNode | None


# Time: O(n), Space: O(n), where n is the number of nodes in the tree.
def recover_tree(root: TreeNode | None) -> None:
    nodes = []

    def dfs(node: TreeNode | None) -> None:
        if node is None:
            return
        dfs(node.left)
        nodes.append(node)
        dfs(node.right)

    dfs(root)
    sorted_vals = sorted([node.val for node in nodes])
    for i in range(len(nodes)):
        nodes[i].val = sorted_vals[i]
