"""
33. Search in Rotated Sorted Array
https://leetcode.com/problems/search-in-rotated-sorted-array/
"""
from math import floor
from typing import List


# O(log n) time, O(1) space, where n is the length of `nums`
def search(nums: List[int], target: int):
    l, r = 0, len(nums) - 1
    is_rotated = nums[0] > nums[-1]
    if is_rotated:
        # Binary search to find index of rotation
        while l < r:
            mid = floor(l + (r - l) / 2)
            if nums[mid] >= nums[0]:
                l = mid + 1
            else:
                r = mid
        if target < nums[0]:
            # search right half
            r = len(nums) - 1
        else:
            # search left half
            r = l - 1
            l = 0
    # Binary search to find target
    while l < r:
        mid = floor(l + (r - l) / 2)
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            r = mid - 1
        else:
            l = mid + 1

    return l if nums[l] == target else -1
