"""
112. Path Sum
https://leetcode.com/problems/path-sum/
"""
from __future__ import annotations
import dataclasses


@dataclasses.dataclass
class TreeNode:
    val: int
    left: TreeNode
    right: TreeNode


# Time: O(n), Space: O(log n), where n is the number of nodes in the binary tree.
def has_path_sum(root: TreeNode | None, target_sum: int) -> bool:
    def dfs(node: TreeNode, current_sum: int) -> bool:
        if not node:
            return False
        current_sum += node.val
        if not (node.left or node.right):
            return current_sum == target_sum
        return dfs(node.left, current_sum) or dfs(node.right, current_sum)

    return dfs(root, 0)
