"""
59. Spiral Matrix II
https://leetcode.com/problems/spiral-matrix-ii/
"""


# Time: O(n^2), Space: O(n^2)
def generate_matrix(n: int) -> list[list[int]]:
    result = [[0 for _ in range(n)] for _ in range(n)]
    value = 1
    min_col_i, max_col_i = 0, n
    min_row_i, max_row_i = 0, n
    while min_col_i <= max_col_i:
        # Horizontal left -> right
        for i in range(min_col_i, max_col_i):
            result[min_row_i][i] = value
            value += 1
        # Vertical top -> bottom
        for i in range(min_row_i + 1, max_row_i):
            result[i][max_col_i - 1] = value
            value += 1
        # Horizontal right -> left
        for i in reversed(range(min_col_i, max_col_i - 1)):
            result[max_row_i - 1][i] = value
            value += 1
        # Vertical bottom -> top
        for i in reversed(range(min_row_i + 1, max_row_i - 1)):
            result[i][min_col_i] = value
            value += 1
        min_col_i += 1
        max_col_i -= 1
        min_row_i += 1
        max_row_i -= 1
    return result
