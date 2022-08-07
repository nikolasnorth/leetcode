"""
111. Minimum Depth of Binary Tree
https://leetcode.com/problems/minimum-depth-of-binary-tree/
"""
from __future__ import annotations
import dataclasses
import collections


@dataclasses.dataclass
class TreeNode:
    val: int
    left: TreeNode
    right: TreeNode


# Time: O(log n), Space: O(2^log n)
def min_depth(root: TreeNode | None) -> int:
    if root is None:
        return 0
    q = collections.deque([(root, 1)])
    while q:
        node, h = q.popleft()
        if not (node.left or node.right):
            return h
        if node.left:
            q.append((node.left, h + 1))
        if node.right:
            q.append((node.right, h + 1))
    return -1  # Should be unreachable
