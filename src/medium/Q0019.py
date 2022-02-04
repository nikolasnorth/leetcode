"""
19. Remove Nth Node From End of List
https://leetcode.com/problems/remove-nth-node-from-end-of-list/
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# O(n) time, O(1) space, where n is the number of nodes in the linked list
def remove_nth_node(head: Optional[ListNode], n: int):
    slow = head
    fast = head
    for i in range(n):
        fast = fast.next
    if not fast:
        head = head.next
        return head
    while fast.next:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next
    return head
