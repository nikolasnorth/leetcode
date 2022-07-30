// 20. Valid Parentheses
// https://leetcode.com/problems/valid-parentheses/

#include <string>

using namespace std;

// Time: O(n), Space: O(n), where n is the size of `s`.
bool is_valid(string s) {
  const unordered_map<char, char> brackets = {
      {'(', ')'},
      {'[', ']'},
      {'{', '}'},
  };
  const auto open = {'(', '[', '{'};
  deque<char> stack;
  for (const char bracket : s) {
    if (find(open.begin(), open.end(), bracket) != open.end()) {
      stack.push_back(bracket);
    } else if (stack.empty()) {
      return false;
    } else {
      const auto top = stack.back();
      stack.pop_back();
      if (brackets.at(top) != bracket) {
        return false;
      }
    }
  }
  return stack.empty();
}
