// 24. Swap Nodes in Pairs
// https://leetcode.com/problems/swap-nodes-in-pairs/

struct ListNode {
  int val_;
  ListNode *next_;

  ListNode() : val_(0), next_(nullptr) {}
  ListNode(int val) : val_(val), next_(nullptr) {}
  ListNode(int val, ListNode *next) : val_(val), next_(next) {}
};

// O(n) time, O(1) space, where n is the number of nodes in the linked list
auto swap_pairs(ListNode *head) -> ListNode * {
  ListNode *dummy = new ListNode(0, head);
  ListNode *prev = dummy, *first = head;
  while (first and first->next_) {
    ListNode *second = first->next_;
    ListNode *start_of_next_pair = second->next_;

    first->next_ = start_of_next_pair;
    second->next_ = first;
    prev->next_ = second;

    prev = first;
    first = start_of_next_pair;
  }
  ListNode *result = dummy->next_;
  delete dummy;
  return result;
}
