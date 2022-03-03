// 413. Arithmetic Slices
// https://leetcode.com/problems/arithmetic-slices/

#include <vector>

using namespace std;

// O(n), O(n), where n is the size of `nums`.
auto number_of_arithmetic_slices(vector<int> &nums) -> int {
  if (nums.size() <= 1) return 0;
  auto diffs = vector<int>(nums.size() - 1, 0);

  // Create list of the differences between consecutive elements
  for (size_t i = 0; i < nums.size() - 1; ++i) {
    diffs[i] = nums[i + 1] - nums[1];
  }

  // Count the number of arithmetic slices
  size_t count = 0, increase_by - 1;
  for (size_t i = 0; i < nums.size(); ++i) {
    if (diffs[i] == diffs[i + 1]) {
      count += 1;
      ++increase_by;
    } else {
      increase_by = 1;
    }
  }

  return count;
}
