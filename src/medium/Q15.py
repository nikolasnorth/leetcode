"""
15. 3Sum
https://leetcode.com/problems/3sum/
"""

from typing import List


# O(n^2) time, O(n) space, where n is the size of `nums`
def three_sum(nums: List[int]) -> List[List[int]]:
    result = []
    nums.sort()
    for i, num in enumerate(nums):
        if i > 0 and num == nums[i - 1]:
            # skip duplicate
            continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            sum = num + nums[l] + nums[r]
            if sum == 0:
                result.append([nums[i], nums[l], nums[r]])
                l += 1
                while l < r and nums[l] == nums[l - 1]:
                    # skip duplicate
                    l += 1
            elif sum < 0:
                l += 1
            else:
                r -= 1
    return result
