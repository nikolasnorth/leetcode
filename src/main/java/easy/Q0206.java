package easy;

/**
 * 206. Reverse Linked List
 * https://leetcode.com/problems/reverse-linked-list/
 */
class Q0206 {

  // O(n) time, O(1) space, where n is the number of nodes in the list
  public ListNode reverseList(ListNode head) {
    ListNode current = head;
    ListNode prev = null;

    while (current != null) {
      ListNode tmp = current.next;
      current.next = prev;
      prev = current;
      current = tmp;
    }
    return prev;
  }

  private final static class ListNode {
    int val;
    ListNode next;
  }
}
