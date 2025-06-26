"""
268. Missing Number
https://leetcode.com/problems/missing-number
"""


# Time: O(nlogn), Space: O(n), where n is the length of nums
def missing_number_1(nums: list[int]) -> int:
    nums.sort()
    n = len(nums)
    expected = 0
    for current in nums:
        if expected != current:
            return expected
        expected += 1
    return n


# Time: O(n), Space: O(n), where n is the length of nums
def missing_number_2(nums: list[int]) -> int:
    s = set(nums)
    for n in range(0, len(nums) + 1):
        if n not in s:
            return n
    return -1


# Time: O(n), Space: O(1), where n is the length of nums
def missing_number_3(nums: list[int]) -> int:
    n = 0
    for i in range(len(nums) + 1):
        n += 1
    return n - sum(nums)
