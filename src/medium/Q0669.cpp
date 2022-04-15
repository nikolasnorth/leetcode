// 669. Trim a Binary Search Tree
// https://leetcode.com/problems/trim-a-binary-search-tree/

struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
};

// Time: O(n), Space: O(log n), where n is the number of nodes in the tree.
auto trim_bst(TreeNode *root, int low, int high) -> TreeNode * {
  if (root == nullptr) {
    return nullptr;
  }
  if (root->val < low) {
    return trim_bst(root->right, low, high);
  }
  if (root->val > high) {
    return trim_bst(root->left, low, high);
  }
  root->left = trim_bst(root->left, low, high);
  root->right = trim_bst(root->right, low, high);
  return root;
}
