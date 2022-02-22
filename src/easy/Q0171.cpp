// 171. Excel Sheet Column Number
// https://leetcode.com/problems/excel-sheet-column-number/

#include <algorithm>
#include <cmath>
#include <string>

using namespace std;

// O(n) time, O(1) space, where n is the size of `column_title`
auto title_to_number(string column_title) -> int {
  reverse(column_title.begin(), column_title.end());
  int num = 0;
  for (int i = 0; i < column_title.size(); ++i) {
    num += (column_title[i] - 'A' + 1) * pow(26, i);
  }
  return num;
}
