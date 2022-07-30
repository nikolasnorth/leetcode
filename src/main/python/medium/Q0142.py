"""
142. Linked List Cycle II
https://leetcode.com/problems/linked-list-cycle-ii/\
"""
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# O(n) time, O(1) space, where n is the number of nodes in the linked list
def detect_cycle(head: Optional[ListNode]):
    if not head and not head.next:
        return None
    slow = head.next
    fast = head.next.next
    while fast and fast.next.next and fast is not slow:
        slow = slow.next
        fast = fast.next.next
    if not fast or not fast.next:
        return None
    slow = head
    while slow is not fast:
        slow = slow.next
        fast = fast.next
    return slow
