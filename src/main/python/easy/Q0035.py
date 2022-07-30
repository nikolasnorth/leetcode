"""
35. Search Insert Position
https://leetcode.com/problems/search-insert-position/
"""


# Time: O(log n), Space: O(1), where n is the size of `nums`.
def search_insert(nums: list[int], target: int) -> int:
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return lo
