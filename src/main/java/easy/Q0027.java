package easy;

/**
 * 27. Remove Element
 * https://leetcode.com/problems/remove-element/
 */
class Q0027 {

  // O(n) time, O(1) space, where n is the length of `nums`
  int removeElement(int[] nums, int val) {
    int k = 0;
    for (int i = 0; i < nums.length; i++) {
      if (nums[i] != val) {
        nums[k] = nums[i];
        k++;
      }
    }
    return k;
  }
}
