// 392. Is Subsequence
// https://leetcode.com/problems/is-subsequence/

#include <string>

using namespace std;

// O(n) time, O(1) space, where n is the max length between `s` and `t`.
auto is_subsequence(string s, string t) -> bool {
  if (t.size() < s.size()) return false;
  size_t start = 0;
  for (const char c : s) {
    auto pos = t.find(c, start);
    if (pos == string::npos) return false;
    start = pos + 1;
  }
  return true;
}
