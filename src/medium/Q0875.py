"""
875. Koko Eating Bananas
https://leetcode.com/problems/koko-eating-bananas/
"""
from typing import List
from math import ceil


# O(nlog m) time, O(1) space,
# where n is the length of `piles` and m is the length of the range [0, `max(piles)`]
def min_eating_speed(piles: List[int], h: int):
    k = max(piles)
    lo, hi = 1, max(piles)
    while lo <= hi:  # Time: O(log m)
        mid = lo + (hi - lo) // 2
        if can_eat(k=mid, piles=piles, h=h):
            k = min(k, mid)
            hi = mid - 1
        else:
            lo = mid + 1
    return k


def can_eat(k: int, piles: List[int], h: int):  # Time: O(n)
    hours = 0
    for pile in piles:
        hours += ceil(pile / k)
    return hours <= h
