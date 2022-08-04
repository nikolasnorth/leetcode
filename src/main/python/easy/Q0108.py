"""
108. Convert Sorted Array to Binary Search Tree
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
"""
from __future__ import annotations
import dataclasses


@dataclasses.dataclass
class TreeNode:
    val: int
    left: TreeNode
    right: TreeNode


# Time: O(n), Space: O(n log n), where n is the size of `nums`.
def sorted_array_to_bst(nums: list[int]) -> TreeNode | None:
    if not nums:
        return None
    mid = len(nums) // 2
    return TreeNode(
        val=nums[mid],
        left=sorted_array_to_bst(nums[:mid]),
        right=sorted_array_to_bst(nums[mid + 1:]),
    )
