package medium;

/**
 * 11. Container With Most Water
 * https://leetcode.com/problems/container-with-most-water/
 */
class Q0011 {

  // O(n) time, O(1) space, where n is the length of `height`
  int maxArea(int[] height) {
    int l = 0, r = height.length - 1, maxArea = 0;
    while (l < r) {
      int area = Math.min(height[l], height[r]) * (r - l);
      maxArea = Math.max(maxArea, area);
      if (height[l] < height[r]) {
        l += 1;
      } else {
        r -= 1;
      }
    }
    return maxArea;
  }
}
