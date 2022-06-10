// 680. Valid Palindrome II
// https://leetcode.com/problems/valid-palindrome-ii/

#include <string>

using namespace std;

// Time: O(n), Space: O(1), where n is the size of `s`.
bool valid_palindrome(string s) {
  bool result1 = true;
  size_t lo = 0;
  size_t hi = s.size() - 1;
  while (lo < hi) {
    if (s[lo] != s[hi]) {
      result1 = false;
      break;
    }
    ++lo;
    --hi;
  }

  size_t cached_lo = lo;
  size_t cached_hi = hi;

  bool result2 = true;
  ++lo;
  while (lo >= 0 and hi < s.size() and lo < hi) {
    if (s[lo] != s[hi]) {
      result2 = false;
      break;
    }
    ++lo;
    --hi;
  }

  lo = cached_lo;
  hi = cached_hi;

  bool result3 = true;
  --hi;
  while (lo >= 0 and hi < s.size() and lo < hi) {
    if (s[lo] != s[hi]) {
      result3 = false;
      break;
    }
    ++lo;
    --hi;
  }

  return result1 or result2 or result3;
}
