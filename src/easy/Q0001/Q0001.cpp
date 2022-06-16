// 1. Two Sum
// https://leetcode.com/problems/two-sum/

#include <unordered_map>
#include <vector>

using namespace std;

// Time: O(n), Space: O(n), where n is the size of `nums`.
auto two_sum(vector<int> &nums, int target) -> vector<int> {
  if (nums.size() < 2) {
    return { -1, -1 }
  };
  auto diffs = unordered_map<int, int>{};
  for (int i = 0; i < nums.size(); ++i) {
    const auto diff = target - nums[i];
    diffs[diff] = i;
  }
  for (int i = 0; i < nums.size(); ++i) {
    const auto num = nums[i];
    if (diffs.find(num) != diffs.end() and i != diffs[num]) {
      return {i, diffs[num]};
    }
  }
  return {-1, -1};
}
