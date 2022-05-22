// 100. Same Tree
// https://leetcode.com/problems/same-tree/

#include <functional>

using namespace std;

struct TreeNode {
  int val;
  TreeNode* left;
  TreeNode* right;
};

// Time: O(n), Space: O(log n), where n is the number of nodes in `p` or `q`,
// whichever has more. This assumes p and q and ~balanced binary trees.
// Otherwise, the space complexity would be O(n).
auto is_same_tree(TreeNode* p, TreeNode*) -> bool {
  function<bool(TreeNode*, TreeNode*)> dfs = [&dfs](TreeNode* p, TreeNode* q) {
    if (!p and !q) return true;
    if (!p or !q) return false;
    if (p->val != q->val) return false;
    return dfs(p->left, q->left) and dfs(p->right, q->right);
  };
  return dfs(p, q);
}
