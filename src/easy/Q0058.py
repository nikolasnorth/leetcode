"""
58. Length of Last Word
https://leetcode.com/problems/length-of-last-word/
"""


# Time: O(n), Space: O(1), where n is the length of `s`.
def length_of_last_word(s: str) -> int:
    i = 0
    while i >= 0 and s[i] == " ":
        i -= 1
    n = 0
    while i >= 0 and s[i] != " ":
        i -= 1
        n += 1
    return n
