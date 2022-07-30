// 1480. Running Sum of 1d Array
// https://leetcode.com/problems/running-sum-of-1d-array/

#include <numeric>
#include <vector>

using namespace std;

// Time: O(n^2), Space: O(n), where n is the size of `nums`.
vector<int> running_sum(vector<int>& nums) {
  vector<int> sums;
  sums.reserve(nums.size());
  for (int i = 0; i < nums.size(); ++i) {
    const auto sum = accumulate(nums.cbegin(), nums.cbegin() + i + 1, int{0});
    sums.push_back(sum);
  }
  return sums;
}

// Time: O(n), Space: O(n), where n is the size of `nums`.
vector<int> running_sum_2(vector<int>& nums) {
  vector<int> sums;
  sums.reserve(nums.size());
  int running_sum = 0;
  for (int i = 0; i < sums.size(); ++i) {
    running_sum += nums[i];
    sums.push_back(running_sum);
  }
  return sums;
}
