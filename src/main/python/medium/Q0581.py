"""
581. Shortest Unsorted Continuous Subarray
https://leetcode.com/problems/shortest-unsorted-continuous-subarray/
"""


# Time: O(nlog n), Space: O(n), where n is the size of `nums`.
def find_unsorted_subarray(nums: list[int]) -> int:
    sorted_nums = sorted(nums)
    smallest_left, largest_right = len(nums) - 1, 0
    for i in range(len(nums)):
        if nums[i] != sorted_nums[i]:
            smallest_left = min(smallest_left, i)
            largest_right = max(largest_right, i)
    if smallest_left == len(nums) - 1:
        return 0
    return largest_right - smallest_left + 1
