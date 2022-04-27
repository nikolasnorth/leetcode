// 59. Spiral Matrix II
// https://leetcode.com/problems/spiral-matrix-ii/

#include <vector>

using namespace std;

// Time: O(n^2), Space: O(n^2)
auto generate_matrix(int n) -> vector<vector<int>> {
  auto result = vector(n, vector(n, 0));
  int value = 1;
  int min_col_i = 0, max_col_i = n;
  int min_row_i = 0, max_row_i = n;
  while (min_col_i <= max_col_i) {
    // Left -> Right
    for (int i = min_col_i; i < max_col_i; ++i) {
      result[min_row_i][i] = value++;
    }
    // Top -> Bottom
    for (int i = min_row_i + 1; i < max_row_i; ++i) {
      result[i][max_col_i - 1] = value++;
    }
    // Right -> Left
    for (int i = max_col_i - 2; i >= min_col_i; --i) {
      result[max_row_i - 1][i] = value++;
    }
    // Bottom -> Top
    for (int i = max_row_i - 2; i > min_col_i; --i) {
      result[i][min_col_i] = value++;
    }
    ++min_col_i, --max_col_i;
    ++min_row_i, --max_row_i;
  }
  return result;
}
