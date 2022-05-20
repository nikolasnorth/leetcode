"""
26. Remove Duplicates from Sorted Array
https://leetcode.com/problems/remove-duplicates-from-sorted-array/
"""


# Time: O(n), Space: O(1), where n is the size of `nums`.
def remove_duplicates(nums: list[int]) -> int:
    left = right = 0
    while right < len(nums):
        while right < len(nums) - 1 and nums[right] == nums[right + 1]:
            right += 1
        nums[left] = nums[right]
        left += 1
        right += 1
    return left
