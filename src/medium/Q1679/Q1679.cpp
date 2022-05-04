// 1679. Max Number of K-Sum Pairs
// https://leetcode.com/problems/max-number-of-k-sum-pairs/

#include <algorithm>
#include <vector>

using namespace std;

// Time: O(n), Space: O(1), where n is the size of `nums`.
int max_operations(vector<int> &nums, int k) {
  sort(nums.begin(), nums.end());
  int count = 0;
  size_t left = 0, right = nums.size() - 1;
  while (left < right) {
    int total = nums[left] + nums[right];
    if (total == k) {
      ++count;
      ++left;
      --right;
    } else if (total < k) {
      ++left;
    } else {
      --right;
    }
  }
  return count;
}
