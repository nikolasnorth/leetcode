// 389. Find the Difference
// https://leetcode.com/problems/find-the-difference/

#include <algorithm>
#include <string>
#include <unordered_map>

using namespace std;

// Time: O(n), Space: O(n), where n is the size of `t`.
char find_the_difference(string& s, string& t) {
  unordered_map<char, int> char_count;
  for (const char c : t) {
    if (char_count.find(c) == char_count.end()) {
      char_count[c] = 1;
    } else {
      char_count[c] += 1;
    }
  }
  for (const char c : s) {
    if (char_count.find(c) != char_count.end()) {
      char_count[c] -= 1;
    }
  }
  const auto op = [](pair<char, int> p) { return p.second > 0; };
  const auto result = find_if(char_count.begin(), char_count.end(), op);
  if (result == char_count.end()) {
    throw runtime_error("`s` and `t` were equal");
  }
  return (*result).first;
}
