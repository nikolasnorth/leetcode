// 11. Container With Most Water
// https://leetcode.com/problems/container-with-most-water/

#include <algorithm>
#include <vector>

using namespace std;

// Time: O(n), Space: O(1), where n is the size of `height`.
auto max_area(vector<int> &height) -> int {
  if (height.size() < 2) {
    return -1;
  }
  int result = 0;
  size_t left = 0, right = height.size() - 1;
  while (left < right) {
    const int x = right - left;
    const int y = min(height[left], height[right]);
    result = max(result, x * y);
    if (height[left] < height[right]) {
      ++left;
    } else {
      --right;
    }
  }
  return result;
}
