// 104. Maximum Depth of Binary Tree
// https://leetcode.com/problems/maximum-depth-of-binary-tree/

struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;

  TreeNode() : val(0), left(nullptr), right(nullptr) {}
  TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
  TreeNode(int x, TreeNode *l, TreeNode *r) : val(x), left(l), right(r) {}
};

// O(n) time, O(log n) space, where n is the number of nodes in the binary tree
auto max_depth(TreeNode *root) -> int {
  if (!root) return 0;

  int left = max_depth(root->left) + 1;
  int right = max_depth(root->right) + 1;
  return left > right ? left : right;
}
