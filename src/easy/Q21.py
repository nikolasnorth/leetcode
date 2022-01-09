"""
21. Merge Two Sorted Lists
https://leetcode.com/problems/merge-two-sorted-lists/
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# O(n) time, O(1) space, where n is the number of nodes in `list1` and `list2`
def merge_two_sorted_lists(list1: Optional[ListNode], list2: Optional[ListNode]):
    dummy = current = ListNode()
    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    current.next = list1 or list2
    return dummy.next
