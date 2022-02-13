// 78. Subsets
// https://leetcode.com/problems/subsets/

#include <functional>
#include <vector>

using namespace std;

// O(n x 2^n) time: There will be 2^n subsets that will be created, and for each
// one, there will be n elements copied, in the worst case.
// O(nlog n) space: At most there will be log n call stacks, and a vector of
// n elements in each.
auto subsets(vector<int> &nums) -> vector<vector<int>> {
  auto result = vector<vector<int>>{};
  auto subset = vector<int>{};

  function<void(int)> dfs = [&](int i) {
    if (i >= nums.size()) {
      result.push_back(subset);
      return;
    }
    subset.push_back(nums[i]);
    dfs(i + 1);
    subset.pop_back();
    dfs(i + 1);
  };

  dfs(0);
  return result;
}
