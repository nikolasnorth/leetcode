// 94. Binary Tree Inorder Traversal
// https://leetcode.com/problems/binary-tree-inorder-traversal/

#include <vector>

using namespace std;

struct TreeNode {
  int val;
  TreeNode* left;
  TreeNode* right;
};

// Time: O(n), Space: O(n), where n is the number of nodes in the list.
auto inorder_traversal(TreeNode* root) -> vector<int> {
  vector<int> result;
  function<void(TreeNode*)> dfs = [&dfs, &result](TreeNode* root) {
    if (root == nullptr) {
      return;
    }
    dfs(root->left);
    result.push_back(root->val);
    dfs(root->right);
  };
  dfs(root);
  return result;
}
