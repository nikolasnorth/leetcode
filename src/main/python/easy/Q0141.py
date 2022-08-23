"""
141. Linked List Cycle
https://leetcode.com/problems/linked-list-cycle/
"""
from __future__ import annotations
import dataclasses


@dataclasses.dataclass
class ListNode:
    val: int
    next: ListNode


# Time: O(n), Space: O(1), where n is the number of nodes in the linked list.
def has_cycle(head: ListNode | None) -> bool:
    if not head or not head.next:
        return False
    slow = head
    fast = head.next.next
    while slow and fast and fast.next:
        if slow is fast:
            return True
        slow = slow.next
        fast = fast.next.next
    return False
