// 1337. The K Weakest Rows in a Matrix
// https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/

#include <algorithm>
#include <utility>
#include <vector>

using namespace std;

// Time: O(m log(n)), Space: O(m), where m is the number of rows and n is the
// number of columns in `mat`.
vector<int> k_weakest_rows(vector<vector<int>>& mat, int k) {
  const auto num_soldiers_in_row = [](const vector<int>& row) {
    if (row[0] == 0) return 0;
    // use binary search to find the last occurrence of a soldier
    int lo = 0, hi = row.size() - 1;
    int res = 0;
    while (lo <= hi) {
      int mid = int(lo + (hi - lo) / 2);
      if (row[mid] == 1) {
        lo = mid + 1;
        res = mid;
      } else {
        hi = mid - 1;
      }
    }
    // lo represents the index of the first civilian in the given row.
    // this number is equivalent to the number of soldiers in the row.
    return res + 1;
  };
  const auto comp = [](pair<size_t, int> left, pair<size_t, int> right) {
    // compare the number of soldiers
    if (left.first != right.first) return left.first < right.first;
    // if there is a tie, return the lower index
    else
      return left.second < right.second;
  };

  // weakest will hold (number_of_1's, row_index)
  vector<pair<size_t, int>> weakest;
  for (int i = 0; i < mat.size(); ++i) {
    auto num_soldiers = num_soldiers_in_row(mat[i]);
    weakest.push_back({num_soldiers, i});
  }
  sort(weakest.begin(), weakest.end(), comp);
  for (auto row : weakest)
    cout << "[" << row.first << " " << row.second << "]"
         << " ";
  cout << "\n";

  vector<int> result;
  transform(weakest.cbegin(), weakest.cend(), back_inserter(result),
            [](const pair<size_t, int>& item) {
              // keep only the row index
              return item.second;
            });
  return {result.cbegin(), result.cbegin() + k};
}
