"""
703. Kth Largest Element in a Stream
https://leetcode.com/problems/kth-largest-element-in-a-stream/
"""
from bisect import insort
from heapq import heapify, heappop, heappush


# Solution 1
class KthLargest1:
    _k: int
    _nums: list[int]

    def __init__(self, k: int, nums: list[int]):
        self._k = k
        self._nums = sorted(nums)

    def add(self, val: int) -> int:
        insort(self._nums, val)
        return self._nums[-self._k]


# Solution 2
class KthLargest2:
    _k: int
    _nums: list[int]

    def __init__(self, k: int, nums: list[int]):
        self._k = k
        self._nums = nums
        heapify(self._nums)
        # Keep at most k largest elements
        while len(self._nums) > self._k:
            heappop(self._nums)

    def add(self, val: int) -> int:
        # Add val to the heap and pop an element (if necessary) to preserve size constraint
        heappush(self._nums, val)
        if len(self._nums) > self._k:
            heappop(self._nums)
        # The minimum value is the k-th largest element
        return self._nums[0]
