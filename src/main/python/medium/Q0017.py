"""
17. Letter Combinations of a Phone Number
https://leetcode.com/problems/letter-combinations-of-a-phone-number/
"""


# Time: O(n 4^n), Space: O(n log n), where n is the length of `digits`.
def letter_combinations(digits: str) -> list[str]:
    digit_to_chars = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z'],
    }
    result: list[str] = []

    def backtrack(i: int, s: string):
        if len(s) == len(digits):
            result.append(s)
            return
        d = digits[i]
        for c in digit_to_chars[d]:
            backtrack(i + 1, s + c)

    if digits != "":
        backtrack(0, "")
    return result
