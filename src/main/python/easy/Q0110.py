"""
110. Balanced Binary Tree
https://leetcode.com/problems/balanced-binary-tree/
"""
from __future__ import annotations
import dataclasses


@dataclasses.dataclass
class TreeNode:
    val: int
    left: TreeNode
    right: TreeNode


# Time: O(n), Space: O(log n), where n is the number of nodes in the binary tree.
def is_balanced(root: TreeNode | None) -> bool:
    def dfs(node: TreeNode | None) -> (int, bool):
        if not node:
            return 0, True
        l_height, l_balanced = dfs(node.left)
        r_height, r_balanced = dfs(node.right)
        if not (l_balanced and r_balanced):
            return -1, False
        if abs(l_height - r_height) > 1:
            return -1, False
        return 1 + max(l_height, r_height), True

    _, balanced = dfs(root)
    return balanced
