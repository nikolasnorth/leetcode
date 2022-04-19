// 99. Recover Binary Search Tree
// https://leetcode.com/problems/recover-binary-search-tree/

#include <functional>
#include <vector>

using namespace std;

struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
};

// Time: O(n), Space: O(n), where n is the number of nodes in the tree.
void recover_tree(TreeNode *root) {
  auto nodes = vector<TreeNode *>();

  function<void(TreeNode *)> dfs = [&dfs, &nodes](TreeNode *node) {
    if (node == nullptr) {
      return;
    }
    dfs(node->left);
    nodes.push_back(node);
    dfs(node->right);
  };

  dfs(root);

  auto sorted_vals = vector<int>();
  sorted_vals.reserve(nodes.size());
  for (const auto &node : nodes) {
    sorted_vals.push_back(node->val);
  }
  sort(sorted_vals.begin(), sorted_vals.end());

  for (int i = 0; i < nodes.size(); ++i) {
    nodes[i]->val = sorted_vals[i];
  }
}
