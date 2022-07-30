// 5. Longest Palindromic Substring
// https://leetcode.com/problems/longest-palindromic-substring/

#include <string>

using namespace std;

// Time: O(n^2), Space: O(n), where n is the length of `s`.
auto longest_palindrome(string s) -> string {
  string longest = "";
  // Check all odd palindromes
  for (int i = 0; i < s.size(); ++i) {
    int l = i, r = i;
    while (l > -1 and r < s.size() and s[l] == s[r]) {
      const int current_len = r - l + 1;
      if (longest.size() < current_len) {
        longest = s.substr(l, current_len);
      }
      --l, ++r;
    }
  }
  // Check all even palindromes
  for (int i = 0; i < s.size() - 1; ++i) {
    int l = i, r = i + 1;
    while (l > -1 and r < s.size() and s[l] == s[r]) {
      const int current_len = r - l + 1;
      if (longest.size() < current_len) {
        longest = s.substr(l, current_len);
      }
      --l, ++r;
    }
  }
  return longest;
}
