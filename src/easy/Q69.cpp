// 69. Sqrt(x)
// https://leetcode.com/problems/sqrtx/


// O(log x) time, O(1) space, where x is the given `x`
auto my_sqrt(int x) -> int {
  unsigned long long lo = 0, hi = x;  // prevent integer overflow for large values of `x`
  while (lo <= hi) {
    auto mid = lo + (hi - lo) / 2;
    auto product = mid * mid;
    if (product == x) return mid;
    if (product < x) lo = mid + 1;
    else hi = mid - 1;
  }
  return lo - 1;
}
