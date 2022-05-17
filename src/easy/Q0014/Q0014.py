"""
14. Longest Common Prefix
https://leetcode.com/problems/longest-common-prefix/
"""


# Time: O(n * m), Space: O(1), where n is the length of the smallest string in `strs`, and m is the size of `strs`.
def longest_common_prefix(strs: list[str]) -> str:
    smallest = min(strs, key=len)
    for i, letter in enumerate(smallest):
        for s in strs:
            if s[i] != letter:
                return smallest[:i]
    return smallest
