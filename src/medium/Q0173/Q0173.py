"""
173. Binary Search Tree Iterator
https://leetcode.com/problems/binary-search-tree-iterator/
"""
from __future__ import annotations
from dataclasses import dataclass


@dataclass
class TreeNode:
    val: int = 0
    left: TreeNode | None = None
    right: TreeNode | None = None


# Time: O(n), Space: O(log n), where n is the number of nodes in the tree.
class BstIterator:
    stack: list[TreeNode]

    def __init__(self, root: TreeNode | None):
        self.stack = []
        self.traverse_left(root)

    def next(self) -> int:
        next_node = self.stack.pop()
        next_val = next_node.val
        self.traverse_left(next_node.right)
        return next_val

    def has_next(self) -> bool:
        return len(self.stack) > 0

    def traverse_left(self, current: TreeNode | None) -> None:
        while current is not None:
            self.stack.append(current)
            current = current.left
