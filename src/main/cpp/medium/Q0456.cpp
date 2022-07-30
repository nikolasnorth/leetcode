// 456. 132 Pattern
// https://leetcode.com/problems/132-pattern/

#include <algorithm>
#include <utility>
#include <vector>

using namespace std;

// Time: O(n), Space: O(n), where n is the size of `nums`.
bool find_132_pattern(vector<int> &nums) {
  // Monotonically decreasing stack of pairs. For each pair p, p[0] is the
  // value maintaining the monotonic property of the stack and p[1] is the
  // minimum value seen as of the time the pair was inserted.
  vector<pair<int, int>> stack;
  auto min_val = nums[0];
  stack.emplace_back(nums[0], nums[0]);
  for (size_t i = 1; i < nums.size(); ++i) {
    while (!stack.empty() and nums[i] >= stack.back().first) {
      stack.pop_back();
    }
    if (!stack.empty() and nums[i] > stack.back().second) {
      return true;
    }
    min_val = min(min_val, nums[i]);
    stack.emplace_back(nums[i], min_val);
  }
  return false;
}
