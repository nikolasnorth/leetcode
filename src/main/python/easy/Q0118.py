"""
118. Pascal's Triangle
https://leetcode.com/problems/pascals-triangle/
"""


# Time: O(n^2), Space: O(n^2), where n is `num_rows`.
def generate(num_rows: int) -> list[list[int]]:
    result = [[1]]
    for _ in range(1, num_rows):
        temp = [0] + result[-1] + [0]
        row: list[int] = []
        for i in range(len(result[-1]) + 1):
            row.append(temp[i] + temp[i + 1])
        result.append(row)
    return result
