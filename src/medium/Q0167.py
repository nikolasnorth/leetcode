"""
167. Two Sum II - Input Array Is Sorted
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
"""

from typing import List


# Time: O(n), Space: O(1), where n is the length of `numbers`.
def two_sum(numbers: List[int], target: int) -> List[int]:
    left, right = 0, len(numbers) - 1
    while left < right:
        x = numbers[left] + numbers[right]
        if x == target:
            return [left + 1, right + 1]
        if x < target:
            left += 1
        else:
            right -= 1
    return [-1, -1]
