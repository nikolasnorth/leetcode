"""
941. Valid Mountain Array
https://leetcode.com/problems/valid-mountain-array/
"""
from typing import List


# O(n) time, O(1) space, where n is the size of `arr`
def valid_mountain_array_1(arr: List[int]):
    if len(arr) < 3:
        return False
    if arr[0] >= arr[1]:
        # Failed to start ascending prior to descending
        return False
    summit_found = False
    for i in range(1, len(arr)):
        diff = arr[i] - arr[i - 1]
        if diff == 0:
            # Must be strictly increasing/decreasing
            return False
        if summit_found and diff > 0:
            # A summit was already found
            return False
        if not summit_found and diff < 0:
            # Reached summit for the first time, start descending
            summit_found = True
    return summit_found


# O(n) time, O(1) space, where n is the size of `arr`
def valid_mountain_array_2(arr: List[int]):
    if len(arr) < 3:
        return False
    l, r = 0, len(arr) - 1
    while l + 1 < len(arr) - 1 and arr[l] < arr[l + 1]:
        l += 1
    while r - 1 > 0 and arr[r - 1] > arr[r]:
        r -= 1
    return l == r
