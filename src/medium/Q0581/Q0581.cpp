// 581. Shortest Unsorted Continuous Subarray
// https://leetcode.com/problems/shortest-unsorted-continuous-subarray/
#include <algorithm>
#include <vector>

using namespace std;

// Time: O(nlog n), Space: O(n), where n is the size of `nums`.
int find_unsorted_subarray(vector<int> &nums) {
  auto sorted_nums = vector(nums.begin(), nums.end());
  sort(sorted_nums.begin(), sorted_nums.end());
  int smallest_left = nums.size(), largest_right = 0;
  for (int i = 0; i < nums.size(); ++i) {
    if (nums[i] != sorted_nums[i]) {
      smallest_left = min(smallest_left, i);
      largest_right = max(largest_right, i);
    }
  }
  if (smallest_left == nums.size()) return 0;
  return largest_right - smallest_left + 1;
}
