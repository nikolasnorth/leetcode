"""
242. Valid Anagram
https://leetcode.com/problems/valid-anagram/
"""


# Time: O(nlog n), Space: O(n)
def is_anagram(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)
