"""
167. Two Sum II - Input Array Is Sorted
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
"""

from typing import List


# O(n) time, O(1) space, where n is the size of `numbers`
def two_sum(numbers: List[int], target: int) -> List[int]:
    l, r = 0, len(numbers) - 1
    while l < r:
        sum = numbers[l] + numbers[r]
        if sum == target:
            return [l + 1, r + 1]
        elif sum < target:
            l += 1
        else:
            r -= 1
    return []
