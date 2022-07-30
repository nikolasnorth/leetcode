// 133. Clone Graph
// https://leetcode.com/problems/clone-graph/

#include <functional>
#include <unordered_map>
#include <vector>

using namespace std;

class Node {
 public:
  int val_;
  vector<Node *> neighbors_;

  Node() : val_(0), neighbors_(nullptr) {}
  Node(int val) : val_(val), neighbors_(nullptr) {}
  Node(int val, vector<int> neighbors) : val_(val), neighbors_(neighbors) {}
};

// O(n + v), O(n), where n is the number of nodes and v is the number of
// vertices in the graph.
auto clone_graph(Node *node) -> Node * {
  if (!node) return nullptr;

  auto visited = unordered_map<Node *, Node *>{};

  function<Node *(Node *)> dfs = [&dfs, &visited](Node *current) {
    if (visited.find(current) != visited.end()) {
      // Node has already been visited
      return visited[current];
    }
    auto copy = new Node(current->val_);
    visited[current] = copy;
    for (const auto n : current->neighbors_) {
      copy->neighbors_.push_back(dfs(n));
    }
    return copy;
  };

  return dfs(node);
}
