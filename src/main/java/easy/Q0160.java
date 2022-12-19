package easy;

// 160. Intersection of Two Linked Lists
// https://leetcode.com/problems/intersection-of-two-linked-lists/
public class Q0160 {

    private record ListNode(int val, ListNode next) {
    }

    // Time: O(n), Space: O(1), where n is the number of nodes in the longest list.
    ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        var lenA = 0;
        var current = headA;
        while (current != null) {
            lenA++;
            current = current.next;
        }
        var lenB = 0;
        current = headB;
        while (current != null) {
            lenB++;
            current = current.next;
        }
        var longList = lenA > lenB ? headA : headB;
        var shortList = lenA > lenB ? headB : headA;
        for (var i = 0; i < Math.abs(lenA - lenB); i++) {
            longList = longList.next;
        }
        while (longList != null && shortList != null) {
            if (longList == shortList) {
                return longList;
            }
            longList = longList.next;
            shortList = shortList.next;
        }
        return null;
    }
}
