"""
144. Binary Tree Preorder Traversal
https://leetcode.com/problems/binary-tree-preorder-traversal/
"""
from __future__ import annotations
import dataclasses


@dataclasses.dataclass
class TreeNode:
    val: int
    left: TreeNode
    right: TreeNode


# Recursive Approach
# Time: O(n), Space: O(n), where n is the number of nodes in the tree.
def preorder_traversal_1(root: TreeNode | None) -> list[int]:
    l: list[int] = []

    def dfs(node: TreeNode | None) -> None:
        if not node:
            return
        l.append(node.val)
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return l


# Iterative Approach
# Time: O(n), Space: O(1), where n is the number of nodes in the tree.
def preorder_traversal_2(root: TreeNode | None) -> list[int]:
    if not root:
        return []
    s = [root]
    l: list[int] = []
    while s:
        n = s.pop()
        l.append(n.val)
        if n.right:
            s.append(n.right)
        if n.left:
            s.append(n.left)
    return l
