// 258. Add Digits
// https://leetcode.com/problems/add-digits/

#include <numeric>
#include <string>

using namespace std;

// Time: O(n), Space: O(n), where n is the number of digits in `num`.
int add_digits(int num) {
  const auto op = [](const char& a, const char& b) {
    return move(a) + (int(b) - int('0'));
  };
  while (num >= 10) {
    const auto digits = to_string(num);
    num = accumulate(digits.begin(), digits.end(), 0, op);
  }
  return num;
}
