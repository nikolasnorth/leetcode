// 897. Increasing Order Search Tree
// https://leetcode.com/problems/increasing-order-search-tree/

#include <functional>
#include <vector>

using namespace std;

struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;

  TreeNode() : val(0), left(nullptr), right(nullptr) {}
  TreeNode(int v) : val(v), left(nullptr), right(nullptr) {}
};

// Time: O(n), Space: O(n), where n is the number of nodes in the tree.
auto increasing_bst(TreeNode *root) -> TreeNode * {
  auto vals = vector<int>{};

  function<void(TreeNode *)> dfs = [&dfs, &vals](TreeNode *node) {
    if (node == nullptr) {
      return;
    }
    dfs(node->left);
    vals.push_back(node->val);
    dfs(node->right);
  };

  dfs(root);
  auto dummy = new TreeNode();
  auto current = dummy;
  for (const int val : vals) {
    current->right = new TreeNode(val);
    current = current->right;
  }
  return dummy->right;
}
