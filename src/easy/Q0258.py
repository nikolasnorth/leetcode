"""
258. Add Digits
https://leetcode.com/problems/add-digits/
"""


# O(n) time, O(n) space, where n is the number of digits in `num`
def add_digits(num: int):
    result = num
    while result >= 10:
        result = sum([int(char) for char in str(result)])
    return result
