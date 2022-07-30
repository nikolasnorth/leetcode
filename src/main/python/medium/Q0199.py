"""
199. Binary Tree Right Side View
https://leetcode.com/problems/binary-tree-right-side-view/
"""

from __future__ import annotations
from collections import deque
from typing import Deque
from dataclasses import dataclass


@dataclass
class TreeNode:
    val: int
    left: TreeNode
    right: TreeNode


# Time: O(n), Space: height of the binary tree or number of nodes in the lowest level, whichever is more.
def right_side_view(root: TreeNode | None) -> list[int]:
    if not root:
        return []
    res = []
    dq: Deque[TreeNode] = deque([root])
    while dq:
        rightmost_node = dq[-1]
        res.append(rightmost_node.val)
        level_size = len(dq)
        for _ in range(level_size):
            node = dq.popleft()
            if node.left:
                dq.append(node.left)
            if node.right:
                dq.append(node.right)
    return res
