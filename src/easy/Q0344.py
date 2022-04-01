"""
344. Reverse String
https://leetcode.com/problems/reverse-string/
"""
from typing import List


def reverse_string(s: List[int]) -> None:
    for i in range(len(s) // 2):
        tmp = s[i]
        s[i] = s[len(s) - i - 1]
        s[len(s) - i - 1] = tmp
