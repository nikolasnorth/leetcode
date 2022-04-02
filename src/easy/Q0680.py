"""
680. Valid Palindrome II
https://leetcode.com/problems/valid-palindrome-ii/
"""


# Time: O(n), Space: O(1), where n is the length of `s`
def valid_palindrome(s: str) -> bool:
    result = True
    lo, hi = 0, len(s) - 1

    # Check if `s` is a palindrome without removing any characters
    while lo < hi:
        if s[lo] != s[hi]:
            break
        lo += 1
        hi -= 1

    old_lo = lo
    old_hi = hi

    # Check if removal of `s[lo]` makes `s` a palindrome
    result_lo = True
    lo += 1
    while lo < hi:
        if s[lo] != s[hi]:
            result_lo = False
            break
        lo += 1
        hi -= 1

    # Reset `lo` and `hi`
    lo = old_lo
    hi = old_hi

    # Check if removal of `s[hi]` makes `s` a palindrome
    result_hi = True
    hi -= 1
    while lo < hi:
        if s[lo] != s[hi]:
            result_hi = False
            break
        lo += 1
        hi -= 1

    return result and (result_lo or result_hi)
