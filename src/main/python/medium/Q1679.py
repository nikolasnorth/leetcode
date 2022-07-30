"""
1679. Max Number of K-Sum Pairs
https://leetcode.com/problems/max-number-of-k-sum-pairs/
"""


# Time: O(n), Space: O(1), where n is the size of `nums`.
def max_operations(nums: list[int], k: int) -> int:
    nums.sort()
    count = 0
    left, right = 0, len(nums) - 1
    while left < right:
        total = nums[left] + nums[right]
        if total == k:
            count += 1
            left += 1
            right -= 1
        elif total < k:
            left += 1
        else:
            right -= 1
    return count
