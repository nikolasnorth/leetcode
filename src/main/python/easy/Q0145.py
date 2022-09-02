"""
145. Binary Tree Postorder Traversal
https://leetcode.com/problems/binary-tree-postorder-traversal/
"""
from __future__ import annotations
import dataclasses


@dataclasses.dataclass
class TreeNode:
    val: int
    left: TreeNode
    right: TreeNode


# Time: O(n), Space: O(nlog n), where n is the number of nodes in the tree.
def postorder_traversal(root: TreeNode) -> list[int]:
    if not root:
        return []
    l: list[int] = []

    def postorder(node: TreeNode) -> None:
        if not node.left and not node.right:
            l.append(node.val)
            return
        if node.left:
            postorder(node.left)
        if node.right:
            postorder(node.right)
        l.append(node.val)

    postorder(root)
    return l
