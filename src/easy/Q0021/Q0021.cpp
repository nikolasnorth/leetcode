// 21. Merge Two Sorted Lists
// https://leetcode.com/problems/merge-two-sorted-lists/

struct ListNode {
  int val;
  ListNode* next;
  ListNode() : val(0), next(nullptr) {}
};

// Time: O(n), Space: O(1), where n is the number of nodes in `list1` or
// `list2`, whichever is greater.
auto merge_two_lists(ListNode* list1, ListNode* list2) -> ListNode* {
  auto dummy = new ListNode();
  auto current = dummy;
  while (list1 != nullptr and list2 != nullptr) {
    if (list1->val < list2->val) {
      current->next = list1;
      list1 = list1->next;
    } else {
      current->next = list2;
      list2 = list2->next;
    }
    current = current->next;
  }
  current->next = list1 != nullptr ? list1 : list2;
  return dummy->next;
}
