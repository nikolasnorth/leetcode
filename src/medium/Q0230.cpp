// 230. Kth Smallest Element in a BST
// https://leetcode.com/problems/kth-smallest-element-in-a-bst/

#include <functional>
#include <vector>

using namespace std;

struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
};

// Time: O(k) if k > log n, otherwise O(log n), where n is the number of nodes
// in the tree.
// Space: O(k)
auto kth_smallest(TreeNode *root, int k) -> int {
  auto vals = vector<int>();
  vals.reserve(k);

  function<void(const TreeNode *)> dfs = [&](const TreeNode *node) {
    if (node == nullptr) {
      return;
    }
    dfs(node->left);
    if (vals.size() < k) {
      vals.push_back(node->val);
    }
    if (vals.size() < k) {
      dfs(node->right);
    }
  };

  dfs(root);
  return vals.back();
}
