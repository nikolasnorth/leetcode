// 171. Excel Sheet Column Number
// https://leetcode.com/problems/excel-sheet-column-number/

#include <algorithm>
#include <cmath>
#include <string>

using namespace std;

// O(n) time, O(1) space, where n is the size of `column_title`
auto title_to_number(string column_title) -> int {
  size_t i = 1, N = columnTitle.size(), col_num = 0;
  for (const char col : columnTitle) {
    col_num += (col - 'A' + 1) * pow(26, N - i);
    ++i;
  }
  return col_num;
}
