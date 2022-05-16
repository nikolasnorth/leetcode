// 13. Roman to Integer
// https://leetcode.com/problems/roman-to-integer/

#include <string>
#include <unordered_map>

using namespace std;

// Time: O(n), Space: O(1), where n is the size of `s`.
int roman_to_int(string s) {
  if (s.size() == 0) {
    return 0;
  }
  unordered_map<char, int> numerals = {
      {'I', 1},   {'V', 5},   {'X', 10},   {'L', 50},
      {'C', 100}, {'D', 500}, {'M', 1000},
  };
  int total = numerals[s[0]];
  for (int i = 1; i < s.size(); ++i) {
    char numeral = s[i];
    char prev_numeral = s[i - 1];
    if (((numeral == 'V' or numeral == 'X') and prev_numeral == 'I') ||
        ((numeral == 'L' or numeral == 'C') and prev_numeral == 'X') ||
        ((numeral == 'D' or numeral == 'M') and prev_numeral == 'C')) {
      total += numerals[numeral] - 2 * numerals[prev_numeral];
    } else {
      total += numerals[numeral];
    }
  }
  return total;
}
