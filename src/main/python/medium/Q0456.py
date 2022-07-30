"""
456. 132 Pattern
https://leetcode.com/problems/132-pattern/
"""


# Time: O(n), Space: O(n), where n is the size of `nums`.
def find_132_pattern(nums: list[int]) -> bool:
    # Monotonically decreasing stack of pairs. For each pair p, p[0] is the
    # value maintaining the monotonic property of the stack and p[1] is the
    # minimum value seen as of the time the pair was inserted.
    stack: list[tuple[int, int]] = []
    min_val = nums[0]
    item = (nums[0], nums[0])
    stack.append(item)
    for n in nums[1:]:
        while len(stack) > 0 and n >= stack[-1][0]:
            stack.pop()
        if len(stack) > 0 and n > stack[-1][1]:
            return True
        min_val = min(min_val, n)
        item = (n, min_val)
        stack.append(item)
    return False
