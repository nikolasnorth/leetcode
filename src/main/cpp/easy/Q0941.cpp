// 941. Valid Mountain Array
// https://leetcode.com/problems/valid-mountain-array/

#include <vector>

using namespace std;

// Time: O(n), Space: O(1), where n is the size of `arr`.
bool valid_mountain_array(vector<int>& arr) {
  size_t lo = 0, hi = arr.size() - 1;
  while (lo < arr.size() - 1 and arr[lo] < arr[lo + 1]) ++lo;
  while (hi > 0 and arr[hi] < arr[hi - 1]) --hi;
  if (lo == arr.size() - 1 or hi == 0) return false;
  return lo == hi;
}
