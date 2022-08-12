"""
119. Pascal's Triangle II
https://leetcode.com/problems/pascals-triangle-ii/
"""


# Time: O(n^2), Space: O(n), where n is `row_index`.
def get_row(row_index: int) -> list[int]:
    prev_row = [1]
    for i in range(1, row_index + 1):
        prev_row = [0] + prev_row + [0]
        curr_row = []
        for j in range(1, len(prev_row)):
            curr_row.append(prev_row[j - 1] + prev_row[j])
        if i == row_index:
            return curr_row
        prev_row = curr_row
    return prev_row
