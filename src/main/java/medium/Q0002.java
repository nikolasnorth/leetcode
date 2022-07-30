package medium;

/**
 * 2. Add Two Numbers
 * https://leetcode.com/problems/add-two-numbers/
 */
class Q0002 {

  // O(n) time, O(n) space, where n is the number of nodes in l1 or l2, whichever is longest
  ListNode addTwoNumbers(ListNode l1, ListNode l2) {
    ListNode current = new ListNode(0);
    ListNode head = current;
    int carry = 0;

    while (l1 != null || l2 != null) {
      if (l1 == null) {
        l1 = new ListNode(0);
      }
      if (l2 == null) {
        l2 = new ListNode(0);
      }
      int sum = l1.val = l2.val + carry;
      if (sum > 9) {
        carry = 1;
        current.next = new ListNode(sum - 10);
      } else {
        carry = 0;
        current.next = new ListNode(sum);
      }
      current = current.next;
      l1 = l1.next;
      l2 = l2.next;
    }
    if (carry == 1) {
      current.next = new ListNode(1);
    }
    return head.next;
  }

  private static class ListNode {
    int val;
    ListNode next;

    ListNode(int val) {
      this.val = val;
    }
  }
}
