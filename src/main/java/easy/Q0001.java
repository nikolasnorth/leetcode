package easy;

import java.util.HashMap;

/**
 * 1. Two Sum
 * https://leetcode.com/problems/two-sum/
 */
class Q0001 {

  // O(n^2) time, O(1) space, where n is the length of nums
  int[] twoSum1(int[] nums, int target) {
    for (int i = 0; i < nums.length - 1; i++) {
      for (int j = i + 1; j < nums.length; j++) {
        if (nums[i] + nums[j] == target) {
          return new int[]{i, j};
        }
      }
    }
    return new int[]{-1, -1};
  }

  // O(n) time, O(n) space, where n is the length of nums
  int[] twoSum2(int[] nums, int target) {
    HashMap<Integer, Integer> results = new HashMap<>(nums.length);
    for (int i = 0; i < nums.length; i++) {
      if (results.containsKey(nums[i])) {
        return new int[]{results.get(nums[i]), i};
      } else {
        results.put(target - nums[i], i);
      }
    }
    return new int[]{-1, -1};
  }
}
