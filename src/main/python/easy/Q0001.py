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
