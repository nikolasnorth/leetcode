"""
20. Valid Parentheses
https://leetcode.com/problems/valid-parentheses/
"""


def is_valid(s: str):
    pairs = {
        ")": "(",
        "}": "{",
        "]": "[",
    }
    stack = []
    for bracket in s:
        if bracket in pairs.values():
            stack.append(bracket)
            continue
        if not stack:
            return False
        if stack.pop() != pairs[bracket]:
            return False
    return len(stack) == 0
