// 165. Compare Version Numbers
// https://leetcode.com/problems/compare-version-numbers/

#include <string>

using namespace std;

// O(n) time, O(n) space, where n is the max size between `version1` and
// `version 2`.
auto compare_version(string version1, string version2) -> int {
  string delim = ".";
  size_t pos = 0;

  // Split version1 into vector of revisions
  auto rev1 = vector<int>{};
  while ((pos = version1.find(delim)) != string::npos) {
    rev1.push_back(stoi(version1.substr(0, pos)));
    version1.erase(0, pos + delim.size());
  }
  rev1.push_back(stoi(version1));

  // Split version2 into vector of revisions
  pos = 0;
  auto rev2 = vector<int>{};
  while ((pos = version2.find(delim)) != string::npos) {
    rev2.push_back(stoi(version2.substr(0, pos)));
    version2.erase(0, pos + delim.size());
  }
  rev2.push_back(stoi(version2));

  // Compare revisions for version1 and version2
  for (size_t i = 0; i < max(rev1.size(), rev2.size()); ++i) {
    int i1 = i < rev1.size() ? rev1[i] : 0;
    int i2 = i < rev2.size() ? rev2[i] : 0;
    if (i1 < i2) return -1;
    if (i1 > i2) return 1;
  }

  return 0;
}
