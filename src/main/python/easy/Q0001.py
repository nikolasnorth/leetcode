"""
1. Two Sum
https://leetcode.com/problems/two-sum/
"""


# Time: O(n), Space: O(n), where n is the length of `nums`.
def two_sum(nums: list[int], target: int) -> list[int]:
    diffs = {}
    for i, n in enumerate(nums):
        diffs[target - n] = i
    for i, n in enumerate(nums):
        diff_i = diffs.get(n)
        if diff_i and diff_i != i:
            return [diff_i, i]
    return [-1, -1]
