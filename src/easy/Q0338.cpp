// 338. Counting Bits
// https://leetcode.com/problems/counting-bits/

#include <bitset>
#include <vector>

using namespace std;

// 1. Brute-force approach:
// O(n) time, O(n) space
auto count_bits_1(int n) -> vector<int> {
  auto ans = vector<int>(n + 1, 0);
  for (int i = 0; i <= n; ++i) {
    auto bits = bitset<32>(i);
    for (const auto bit : bits.to_string()) {
      if (bit == '1') ans[i] += 1;
    }
  }
  return ans;
}

// 2. Dynamic programming approach (more optimal than brute-force):
// O(n) time, O(n) space
auto count_bits_2(int n) -> vector<int> {
  auto ans = vector<int>(n + 1, 0);
  int offset = 1;
  for (int i = 1; i <= n; ++i) {
    if (i == offset * 2) {
      offset = i;
    }
    ans[i] = 1 + ans[i - offset];
  }
  return ans;
}
