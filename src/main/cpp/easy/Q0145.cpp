// 145. Binary Tree Postorder Traversal
// https://leetcode.com/problems/binary-tree-postorder-traversal/
#include <iostream>
#include <vector>

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;

    TreeNode() : val(0), left(nullptr), right(nullptr) {}

    TreeNode(int i) : val(i), left(nullptr), right(nullptr) {}
};

// Time: O(n), Space: O(nlog n), where n is the number of nodes in the tree.
auto postorder_traversal(TreeNode *root) -> std::vector<int> {
    if (!root) return {};

    std::vector<int> v;

    std::function<void(TreeNode *)> traverse = [&traverse, &v](const TreeNode *node) -> void {
        if (!node) throw std::invalid_argument("node cannot be null");

        if (!node->left and !node->right) {
            v.push_back(node->val);
            return;
        }
        if (node->left) {
            traverse(node->left);
        }
        if (node->right) {
            traverse(node->right);
        }
        v.push_back(node->val);
    };

    traverse(root);
    return v;
}
