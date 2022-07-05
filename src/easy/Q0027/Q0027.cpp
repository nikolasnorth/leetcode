// 27. Remove Element
// https://leetcode.com/problems/remove-element/

#include <vector>

using namespace std;

// Time: O(n), Space: O(1), where n is the size of `nums`.
auto remove_element(vector<int>& nums, int val) -> int {
  size_t i = 0;
  for (size_t j = 0; j < nums.size(); ++j) {
    if (nums[j] != val) {
      nums[i] = nums[j];
      ++i;
    }
  }
  return i
}
