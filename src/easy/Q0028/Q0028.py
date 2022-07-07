"""
28. Implement strStr()
https://leetcode.com/problems/implement-strstr/
"""


# Time: O(nm), Space: O(1), where n is the size of `haystack` and m is the size of `needle`.
def str_str(haystack: str, needle: str) -> int:
    if len(needle) == 0:
        return 0
    for i in range(len(haystack) - len(needle) + 1):
        if needle == haystack[i: i + len(needle)]:
            return i
    return -1
