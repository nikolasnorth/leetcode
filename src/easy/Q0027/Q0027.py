"""
27. Remove Element
https://leetcode.com/problems/remove-element/
"""


# Time: O(n), Space: O(1), where n is the size of `nums`.
def remove_element(nums: list[int], val: int) -> int:
    i = 0
    for j in range(len(nums)):
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1
    return i
