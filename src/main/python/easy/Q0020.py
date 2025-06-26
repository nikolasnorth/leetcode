"""
20. Valid Parentheses
https://leetcode.com/problems/valid-parentheses/
"""


# Time: O(n), Space: O(n), where n is the length of `s`
def is_valid(s: str):
    brackets = {
            '(': ')',
            '{': '}',
            '[': ']',
        }
    stack = []
    for bracket in s:
        if bracket in brackets.keys():
            stack.append(bracket)
        elif stack:
            open_bracket = stack.pop()
            if brackets[open_bracket] != bracket:
                return False
        else:
            return False
    return not stack
