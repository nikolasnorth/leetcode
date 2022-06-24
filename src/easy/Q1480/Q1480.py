"""
1480. Running Sum of 1d Array
https://leetcode.com/problems/running-sum-of-1d-array/
"""


# Time: O(n), Space: O(n), where n is the size of `nums`.
def running_sum(nums: list[int]) -> list[int]:
    sums, run = [], 0
    for i in range(len(nums)):
        run += nums[i]
        sums.append(run)
    return sums
