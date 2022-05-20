// 26. Remove Duplicates from Sorted Array
// https://leetcode.com/problems/remove-duplicates-from-sorted-array/

#include <vector>

using namespace std;

// Time: O(n), Space: O(1), where n is the size of `nums`.
int remove_duplicates(vector<int>& nums) {
  size_t left = 0, right = 0;
  while (right < nums.size()) {
    while (right < nums.size() - 1 and nums[right] == nums[right + 1]) {
      ++right;
    }
    nums[left] = nums[right];
    ++left;
    ++right;
  }
  return left;
}
