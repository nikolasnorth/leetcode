// 700. Search in a Binary Search Tree
// https://leetcode.com/problems/search-in-a-binary-search-tree/

struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
};

// Time: O(n), Space: O(log n), where n is the number of nodes in the binary
// tree.
auto search_bst(TreeNode *root, int val) -> TreeNode * {
  if (root == nullptr) {
    return nullptr;
  }
  if (root->val == val) {
    return root;
  }
  auto l = search_bst(root->left, val);
  auto r = search_bst(root->right, val);
  return l ? l : r;
}
