// 136. Single Number
// https://leetcode.com/problems/single-number/

#include <vector>

using namespace std;

// O(n) time, O(1) space, where n is the size of `nums`
auto single_number(vector<int> &nums) -> int {
  int result = 0;
  for (int num : nums) {
    result ^= num;
  }
  return result;
}
