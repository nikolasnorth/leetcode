"""
15. 3Sum
https://leetcode.com/problems/3sum/
"""

from typing import List


# O(n^2) time, O(n) space, where n is the size of `nums`
def three_sum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    solution_set = []
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            triplet_sum = nums[i] + nums[l] + nums[r]
            if triplet_sum == 0:
                solution_set.append([nums[i], nums[l], nums[r]])
                l += 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
            elif triplet_sum < 0:
                l += 1
            else:
                r -= 1
    return solution_set
