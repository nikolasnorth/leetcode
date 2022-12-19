package easy;

// 21. Merge Two Sorted Lists
// https://leetcode.com/problems/merge-two-sorted-lists
public class Q0021 {

    private static class ListNode {
        int val;
        ListNode next;
    }

    // Time: O(n), Space: O(n), where n is the length of list1 or list2, whichever is greater.
    ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        var dummy = new ListNode();
        var current = dummy;
        while (list1 != null && list2 != null) {
            if (list1.val < list2.val) {
                current.next = list1;
                list1 = list1.next;
            } else {
                current.next = list2;
                list2 = list2.next;
            }
            current = current.next;
        }
        current.next = list1 != null ? list1 : list2;
        return dummy.next;
    }
}
