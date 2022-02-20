// 1288. Remove Covered Intervals
// https://leetcode.com/problems/remove-covered-intervals/

#include <vector>

using namespace std;

auto remove_covered_intervals(vector<vector<int>> &intervals) -> int {
  // Sort intervals by leftmost points from smallest to largest.
  // When leftmost points are equal, sort by rightmost points from largest to
  // smallest.
  auto comp = [](const vector<int> &lhs, const vector<int> &rhs) {
    if (lhs[0] < rhs[0]) return true;
    if (lhs[0] > rhs[0]) return false;
    return lhs[1] > rhs[1];
  };
  sort(intervals.begin(), intervals.end(), comp);

  // Build list of all uncovered intervals
  auto uncovered = vector<vector<int>>{intervals[0]};
  bool skip = true;
  for (const auto &current : intervals) {
    // Skip past 1st interval since it was already added
    if (skip) {
      skip = false;
      continue;
    }

    // Compare current with previous uncovered interval
    const auto prev = uncovered.back();
    if (prev[0] <= current[0] and prev[1] >= current[1]) continue;  // covered
    uncovered.push_back(current);
  }

  return uncovered.size();
}
