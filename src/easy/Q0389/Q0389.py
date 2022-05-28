"""
389. Find the Difference
https://leetcode.com/problems/find-the-difference/
"""


# Dictionary Approach
# O(n) time, O(n) space, where n is the number of characters in s
def find_the_difference_1(s: str, t: str):
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
    for char in t:
        if count.get(char, 0) == 0:
            return char
        else:
            count[char] -= 1
    return ""


# Unicode Difference Approach
# O(n) time, O(1) space, where n is the number of characters in s
def find_the_difference_2(s: str, t: str):
    result = i = 0
    while i < len(s):
        result += ord(t[i]) - ord(s[i])
        i += 1
    result += ord(t[i])
    return chr(result)
