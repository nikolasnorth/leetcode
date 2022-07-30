"""
69. Sqrt(x)
https://leetcode.com/problems/sqrtx/
"""


# Time: O(log x), Space: O(1).
def my_sqrt(x: int) -> int:
    lo, hi = 0, x
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        sqr = mid * mid
        if sqr == x:
            return mid
        elif sqr < x:
            lo = mid + 1
        else:
            hi = mid - 1
    return lo - 1
