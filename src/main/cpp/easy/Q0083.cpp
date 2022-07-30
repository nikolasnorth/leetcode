// 83. Remove Duplicates from Sorted List
// https://leetcode.com/problems/remove-duplicates-from-sorted-list/

struct ListNode {
  int val;
  ListNode* next;
};

// Time: O(n), Space: O(1), where n is the number of nodes in the list.
auto delete_duplicates(ListNode* head) -> ListNode* {
  auto current = head;
  while (current != nullptr) {
    while (current->next != nullptr and current->val == current->next->val) {
      auto next = current->next;
      current->next = next->next;
      delete next;
    }
    current = current->next;
  }
  return head;
}
