// 402. Remove K Digits
// https://leetcode.com/problems/remove-k-digits/

#include <deque>
#include <string>

using namespace std;

// O(n) time, O(n) space, where n is the number of characters in `num`
auto remove_k_digits(string num, int k) -> string {
  auto stack = deque<char>{};
  for (char digit : num) {
    while (k > 0 and !stack.empty() and stack.back() > digit) {
      stack.pop_back();
      --k;
    }
    if (stack.empty() and digit == '0') continue;  // skip leading zeroes
    stack.push_back(digit);
  }
  while (k > 0 and !stack.empty()) {
    // At this point, the digits in `stack` are either all equal to each other
    // or in descending order, where the topmost digit is the largest. Removing
    // the topmost digit will result in the lowest possible remaining value.
    stack.pop_back();
    --k;
  }
  return stack.empty() ? "0" : string(stack.begin(), stack.end());
}
