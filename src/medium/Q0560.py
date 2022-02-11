"""
560. Subarray Sum Equals K
https://leetcode.com/problems/subarray-sum-equals-k/
"""
from typing import List


# O(n) time, O(n) space, where n is the size of `nums`
def subarray_sum(nums: List[int], k: int):
    count = current_sum = 0
    prev_sums = {0: 1}
    for num in nums:
        current_sum += num
        count += prev_sums.get(current_sum - k, 0)
        prev_sums[current_sum] = prev_sums.get(current_sum, 0) + 1
    return count
