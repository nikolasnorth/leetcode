// 148. Sort List
// https://leetcode.com/problems/sort-list/

struct ListNode {
  int val_;
  ListNode *next_;

  ListNode() : val_(0), next_(nullptr) {}
  ListNode(int x) : val_(x), next_(nullptr) {}
  ListNode(int x, ListNode *next) : val_(x), next_(next) {}
};

// O(nlog n) time, O(log n) space, where n is the number of nodes in the linked
// list.
auto sort_list(ListNode *head) -> ListNode * {
  if (!head or !head->next) return head;

  // Split list in half
  auto left = head;
  auto slow = head;
  auto fast = head->next;
  while (fast and fast->next) {
    slow = slow->next;
    fast = fast->next->next;
  }
  auto right = slow->next;
  slow->next = nullptr;

  // Sort left and right
  left = sortList(left);
  right = sortList(right);

  // Merge left and right
  auto dummy = new ListNode();
  auto sorted = dummy;
  while (left and right) {
    if (left->val < right->val) {
      sorted->next = left;
      left = left->next;
    } else {
      sorted->next = right;
      right = right->next;
    }
    sorted = sorted->next;
  }
  if (left) sorted->next = left;
  if (right) sorted->next = right;

  return dummy->next;
}
