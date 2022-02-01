"""
69. Sqrt(x)
https://leetcode.com/problems/sqrtx/
"""


# O(log x) time, O(1) space, where x is the given `x`
def my_sqrt(x: int):
    lo, hi = 0, x
    while lo <= hi:
        mid = lo + (hi - lo // 2)
        product = mid * mid
        if product == x:
            return mid
        if product < x:
            lo = mid + 1
        else:
            hi = mid - 1
    return lo - 1
