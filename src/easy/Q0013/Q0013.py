"""
13. Roman to Integer
https://leetcode.com/problems/roman-to-integer/
"""


# Time: O(n), Space: O(1), where n is the size of `s`.
def roman_to_int(s: str) -> int:
    if len(s) == 0:
        return 0
    numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    total = numerals[s[0]]
    for i in range(1, len(s)):
        numeral = s[i]
        if numeral in ['V', 'X'] and s[i - 1] == 'I':
            total += numerals[numeral] - 2 * numerals['I']
        elif numeral in ['L', 'C'] and s[i - 1] == 'X':
            total += numerals[numeral] - 2 * numerals['X']
        elif numeral in ['D', 'M'] and s[i - 1] == 'C':
            total += numerals[numeral] - 2 * numerals['C']
        else:
            total += numerals[numeral]
    return total
