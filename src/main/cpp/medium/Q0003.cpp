// 3. Longest Substring Without Repeating Characters
// https://leetcode.com/problems/longest-substring-without-repeating-characters/

#include <string>
#include <unordered_set>

using namespace std;

// Time: O(n), Space: O(n), where n is the size of `s`.
auto length_of_longest_substring(string s) -> int {
  size_t l = 0, longest = 0;
  auto visited = unordered_set<char>{};
  for (size_t r = 0; r < s.size(); ++r) {
    auto pos_r = visited.find(s[r]);
    while (pos_r != visited.end()) {
      const auto pos_l = visited.find(s[l]);
      visited.erase(pos_l);
      ++l;
      pos_r = visited.find(s[r]);
    }
    visited.insert(s[r]);
    longest = max(longest, visited.size());
  }
  return static_cast<int>(longest);
}
