// 169. Majority Element
// https://leetcode.com/problems/majority-element/

#include <vector>

using namespace std;

// O(n) time, O(1) space, where n is the size of `nums`.
auto majority_element(vector<int> &nums) -> int {
  // Boyer-Moore majority vote algorithm
  int major = nums[0], count = 1;
  for (int i = 1; i < nums.size(); ++i) {
    if (count == 0) {
      major = nums[1];
      ++count;
    } else if (nums[i] == major) {
      ++count;
    } else {
      --count;
    }
  }
  return major;
}
