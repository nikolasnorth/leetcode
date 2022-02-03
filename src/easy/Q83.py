"""
83. Remove Duplicates from Sorted List
https://leetcode.com/problems/remove-duplicates-from-sorted-list/
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# O(n) time, O(1) space, where n is the number of nodes in the linked list
def delete_duplicates_1(head: Optional[ListNode]):
    if not head:
        return None
    slow, fast = head, head.next
    while fast:
        if slow.val == fast.val:
            slow.next = fast.next
        else:
            slow = slow.next
        fast = fast.next
    return head


# O(n) time, O(1) space, where n is the number of nodes in the linked list
def delete_duplicates_2(head: Optional[ListNode]):
    if not head or not head.next:
        return head
    current = head
    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    return head
