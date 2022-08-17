"""
125. Valid Palindrome
https://leetcode.com/problems/valid-palindrome/
"""


# Time: O(n), Space: O(n), where n is the size of `s`.
def is_palindrome(s: str) -> bool:
    s = "".join(c for c in s if c.isalnum()).lower()
    l, r = 0, len(s) - 1
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True
