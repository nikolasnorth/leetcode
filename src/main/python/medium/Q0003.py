"""
3. Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters
"""


# Time: O(n), Space: O(n), where n is the length of s
def length_of_longest_substring(s: string) -> int:
    longest = 0
    unique = set()
    l = 0
    for r in range(len(s)):
        while s[r] in unique:
            unique.remove(s[l])
            l += 1
        unique.add(s[r])
        longest = max(longest, len(unique))
    return longest
