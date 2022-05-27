// 344. Reverse String
// https://leetcode.com/problems/reverse-string/

#include <vector>

using namespace std;

// Time: O(n), Space: O(1), where n is the size of `s`.
void reverse_string(vector<char>& s) {
  for (size_t left = 0; left < s.size() / 2; ++left) {
    const size_t right = s.size() - 1 - left;
    const auto tmp = s[left];
    s[left] = s[right];
    s[right] = tmp;
  }
}
