"""
9. Palindrome Number
https://leetcode.com/problems/palindrome-number/
"""


# Time: O(n), Space(n), where n is the number of digits in `x`.
def is_palindrome(x: int) -> bool:
    s = str(x)
    lo, hi = 0, len(s) - 1
    while lo < hi:
        if s[lo] != s[hi]:
            return False
        lo += 1
        hi -= 1
    return True
