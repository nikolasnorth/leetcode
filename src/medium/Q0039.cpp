// 39. Combination Sum
// https://leetcode.com/problems/combination-sum/

#include <functional>
#include <numeric>
#include <vector>

using namespace std;

// O(2^(t/m)) time, O(t/m) space, where t is the `target` value and m is the
// minimum value in `candidates`.
// Explanation:
// This is a depth-first-search recursive solution with a branching factor of 2.
// The base case occurs when the sum of the elements of the `current` vector is
// greater to or equal to `target`. Therefore, `current` will have at most
// `target/min(candidates)` elements.
auto combination_sum(vector<int> &candidates, int target) {
  auto combinations = vector<vector<int>>{};
  auto current = vector<int>{};

  function<void(int)> dfs = [&](int start) {
    auto total = accumulate(current.begin(), current.end(), 0);
    if (start >= candidates.size() or total > target) return;
    if (total == target) {
      combinations.push_back(current);
      return;
    }
    current.push_back(candidates[start]);
    dfs(start);
    current.pop_back();
    dfs(start + 1);
  };

  dfs(0);
  return combinations;
}
