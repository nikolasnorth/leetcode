// 173. Binary Search Tree Iterator
// https://leetcode.com/problems/binary-search-tree-iterator/
#include <stack>

using namespace std;

struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
};

// Time: O(n), Space: O(log n), where n is the number of nodes in the tree.
class BstIterator {
 private:
  stack<TreeNode *> s{};

 public:
  BstIterator(TreeNode *root) { traverse_left(root); }

  int next() {
    auto next_node = s.top();
    const auto next_val = next_node->val;
    s.pop();
    traverse_left(next_node->right);
    return next_val;
  }

  bool has_next() { return !s.empty(); }

  void traverse_left(TreeNode *current) {
    while (current != nullptr) {
      s.push(current);
      current = current->left;
    }
  }
};
