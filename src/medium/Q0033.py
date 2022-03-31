"""
33. Search in Rotated Sorted Array
https://leetcode.com/problems/search-in-rotated-sorted-array/
"""
from typing import List


# Time: O(log n), Space: O(1), where n is the length of `nums`
def search(nums: List[int], target: int):
    lo, hi = 0, len(nums) - 1
    is_rotated = nums[0] > nums[-1]
    if is_rotated:
        # Find index of rotation
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] >= nums[0]:
                lo = mid + 1
            else:
                hi = mid
        # Reset lo and hi depending on target
        if target == nums[0]:
            return 0
        if target < nums[0]:
            # Search right from point of rotation
            hi = len(nums) - 1
        else:
            # Search left from point of rotation
            hi = lo - 1
            lo = 0
    # Binary search to find target
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            hi = mid - 1
        else:
            lo = mid + 1

    return lo if nums[lo] == target else -1
