"""
1209. Remove All Adjacent Duplicates in String II
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/
"""


# Time: O(n), Space: O(n), where n is the size of `s`.
def remove_duplicates(s: str, k: int) -> str:
    # Stack containing (char, count) tuples
    stack: list[tuple[str, int]] = []
    for c in s:
        if len(stack) == 0:
            item = (c, 1)
            stack.append(item)
            continue
        top: tuple[str, int] = stack[-1]
        if top[0] != c:
            item = (c, 1)
            stack.append(item)
            continue
        count = top[1] + 1
        if count == k:
            stack.pop()
            continue
        item = (c, count)
        stack[-1] = item
    result = ""
    for item in stack:
        c, count = item
        result += c * count
    return result
