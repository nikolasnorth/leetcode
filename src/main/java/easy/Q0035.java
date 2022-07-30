package easy;

/**
 * 35. Search Insert Position
 * https://leetcode.com/problems/search-insert-position/
 */
class Q0035 {

  // O(logn) time, O(1) space, where n is the length of `nums`
  int searchInsert(int[] nums, int target) {
    if (target < nums[0]) {
      return 0;
    }
    if (target > nums[nums.length - 1]) {
      return nums.length;
    }
    int l = 0;
    int r = nums.length - 1;
    while (l <= r) {
      int mid = l + Math.floorDiv(r - l, 2);
      if (nums[mid] == target) {
        return mid;
      }
      if (nums[mid] < target) {
        l = mid + 1;
      } else {
        r = mid - 1;
      }
    }
    return l;
  }
}
