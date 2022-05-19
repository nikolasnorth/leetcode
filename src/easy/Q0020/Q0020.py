"""
20. Valid Parentheses
https://leetcode.com/problems/valid-parentheses/
"""


# Time: O(n), Space: O(n), where n is the length of `s`
def is_valid(s: str):
    pairs = {")": "(", "}": "{", "]": "["}
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
