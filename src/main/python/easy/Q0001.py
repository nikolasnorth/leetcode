"""
1. Two Sum
https://leetcode.com/problems/two-sum/
"""


# Time: O(n), Space: O(n), where n is the length of `nums`.
def two_sum(nums: list[int], target: int) -> list[int]:
    visited = {}
    for i, n in enumerate(nums):
        diff = target - n
        if diff in visited:
            return [i, visited[diff]]
        visited[n] = i
    return [-1, -1]


# Time: O(n^2), Space: O(1), where n is the length of nums.
def two_sum_2(nums: list[int], target: int) -> list[int]:
    for i, i_val in enumerate(nums):
        for j, j_val in enumerate(nums):
            if i == j:
                continue
            if i_val + j_val == target:
                return [i, j]
    return [-1, -1]