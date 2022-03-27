"""
1337. The K Weakest Rows in a Matrix
https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/
"""
from typing import List


# Time: O(m log(n)), Space: O(m), where m and n are the number of rows and
# columns in `mat`, respectively.
def k_weakest_rows(mat: List[List[int]], k: int) -> List[int]:
    weakest = []
    for i in range(len(mat)):
        num_soldiers = num_soldiers_in(mat[i])
        weakest.append((num_soldiers, i))
    weakest.sort(key=lambda row: (row[0], row[1]))
    return [row[1] for row in weakest[:k]]


def num_soldiers_in(row: List[int]) -> int:
    if row[0] == 0:
        return 0
    lo, hi = 0, len(row) - 1
    res = 0
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if row[mid] == 1:
            res = mid
            lo = mid + 1
        else:
            hi = mid - 1
    return res + 1
