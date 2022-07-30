// 14. Longest Common Prefix
// https://leetcode.com/problems/longest-common-prefix/

#include <string>
#include <vector>

using namespace std;

// Time: O(n * m), Space: O(1), where n is the length of the smallest string in
// `strs`, and m is the size of `strs`.
auto longest_common_prefix(vector<string>& strs) -> string {
  const auto comp = [](const string& a, const string& b) {
    return a.size() < b.size();
  };
  const auto smallest = min_element(strs.begin(), strs.end(), comp);
  for (int i = 0; i < smallest->size(); ++i) {
    const auto c = (*smallest)[i];
    for (const auto& s : strs) {
      if (c != s[i]) {
        return string(smallest->begin(), smallest->begin() + i);
      }
    }
  }
  return *smallest;
}
