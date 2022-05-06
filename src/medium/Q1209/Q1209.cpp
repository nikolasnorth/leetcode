// 1209. Remove All Adjacent Duplicates in String II
// https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/
#include <string>
#include <utility>
#include <vector>

using namespace std;

// Time: O(n), Space: O(n), where n is the size of `s`.
auto remove_duplicates(string s, int k) -> string {
  auto stack = vector<pair<char, size_t>>();
  for (const auto c : s) {
    if (stack.empty()) {
      stack.emplace_back(c, 1);
      continue;
    }
    auto &top = stack.back();
    if (top.first != c) {
      stack.emplace_back(c, 1);
      continue;
    }
    if (top.second + 1 == k) {
      stack.pop_back();
      continue;
    }
    // Increment count of 'c'
    ++top.second;
  }
  string result;
  for (const auto &[c, count] : stack) {
    result += string(count, c);
  }
  return result;
}
