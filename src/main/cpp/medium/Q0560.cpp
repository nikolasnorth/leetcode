// 560. Subarray Sum Equals K
// https://leetcode.com/problems/subarray-sum-equals-k/

#include <unordered_map>
#include <vector>

using namespace std;

// O(n) time, O(n) space, where n is the size of `nums`
auto subarray_sum(vector<int> &nums, int k) -> int {
  unsigned int count = 0;
  int current_sum = 0;
  auto prev_sums = unordered_map<int, unsigned int>{{0, 1}};
  for (auto num : nums) {
    current_sum += num;
    if (prev_sums.find(current_sum - k) != prev_sums.end()) {
      count += prev_sums[current_sum - k];
    }
    if (prev_sums.find(current_sum) == prev_sums.end()) {
      prev_sums[current_sum] = 1;
    } else {
      prev_sums[current_sum] += 1;
    }
  }
  return count;
}
