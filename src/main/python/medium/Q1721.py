"""
1721. Swapping Nodes in a Linked List
https://leetcode.com/problems/swapping-nodes-in-a-linked-list/
"""

from __future__ import annotations
from dataclasses import dataclass


@dataclass
class ListNode:
    val: int = 0
    next: ListNode = None


# Time: O(n), Space: O(1), where n is the length of the given linked list.
def swap_nodes(head: ListNode | None, k: int) -> ListNode | None:
    lo = hi = tmp = head
    # Set lo equal to the k-th node from the beginning
    for i in range(k - 1):
        lo = lo.next
    # Set hi equal to the k-th node from the end
    for i in range(k):
        tmp = tmp.next
    while tmp:
        tmp = tmp.next
        hi = hi.next
    # Swap values for lo and hi
    tmp_val = lo.val
    lo.val = hi.val
    hi.val = tmp_val

    return head
