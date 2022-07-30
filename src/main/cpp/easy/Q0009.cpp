// 9. Palindrome Number
// https://leetcode.com/problems/palindrome-number/

#include <string>

using namespace std;

// Time: O(n), Space: O(1), where n is the number of digits in `x`.
bool is_palindrome(int x) {
  auto x_str = to_string(x);
  size_t left = 0, right = x_str.size() - 1;
  while (left < right) {
    if (x_str[left] != x_str[right]) {
      return false;
    }
    ++left;
    --right;
  }
  return true;
}
