package easy;

import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

/**
 * 234. Palindrome Linked List
 * https://leetcode.com/problems/palindrome-linked-list/
 */
class Q0234 {

  // O(n) time, O(n) space, where n is the number of nodes in the linked list
  boolean isPalindrome1(ListNode head) {
    // Copy all values from the linked list into an array
    List<Integer> values = new ArrayList<>();
    ListNode current = head;
    while (current != null) {
      values.add(current.val);
      current = current.next;
    }

    // Compare values at opposite ends to check if the list is a palindrome
    for (int i = 0; i < Math.floorDiv(values.size(), 2); i++) {
      if (!Objects.equals(values.get(i), values.get(values.size() - 1 - i))) {
        return false;
      }
    }

    return true;
  }

  // O(n) time, O(1) space, where n is the number of nodes in the list
  boolean isPalindrome2(ListNode head) {
    // Advance pointer to middle of the list
    ListNode slow = head;
    ListNode fast = head;
    while (fast != null && fast.next != null) {
      slow = slow.next;
      fast = fast.next.next;
    }

    // Reverse 2nd half of list
    ListNode prev = null;
    ListNode current = slow;
    while (current != null) {
      ListNode tmp = current.next;
      current.next = prev;
      prev = current;
      current = tmp;
    }

    // Compare nodes at opposite ends to check if list is a palindrome
    ListNode n1 = head;
    ListNode n2 = prev;
    while (n2 != null) {
      if (n1.val != n2.val) {
        return false;
      }
      n1 = n1.next;
      n2 = n2.next;
    }

    return true;
  }

  private final static class ListNode {
    int val;
    ListNode next;
  }
}
