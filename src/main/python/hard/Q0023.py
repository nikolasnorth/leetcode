"""
23. Merge k Sorted Lists
https://leetcode.com/problems/merge-k-sorted-lists/
"""
from queue import PriorityQueue
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Helper function for `merge_k_sorted_lists_1()`
def merge_two_sorted_lists(list1, list2):
    dummy = current = ListNode()
    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    if list1:
        current.next = list1
    if list2:
        current.next = list2
    return dummy.next


# O(nlog(m)) time, O(m) space, where m is the size of `lists` and n is the combined of nodes
def merge_k_sorted_lists_1(lists: List[Optional[ListNode]]):
    if not lists:
        return None
    while len(lists) > 1:
        merged_lists = []
        for i in range(0, len(lists), 2):
            list1 = lists[i]
            list2 = lists[i + 1] if i + 1 < len(lists) else None
            merged_lists.append(merge_two_sorted_lists(list1, list2))
        lists = merged_lists
    return lists[0]


# O(nlog(m)) time, O(m) space, where m is the size of `lists` and n is the combined number of nodes
def merge_k_sorted_lists_2(lists: List[Optional[ListNode]]):
    dummy = current = ListNode()
    q = PriorityQueue(maxsize=len(lists))
    for i, node in enumerate(lists):  # O(m)
        if node:
            q.put((node.val, i, node))
    while q.qsize() > 0:  # O(n)
        _, i, node = q.get()
        current.next = node
        current = current.next
        if node.next:
            q.put((node.next.val, i, node.next))  # O(log m)
    return dummy.next
