// 1672. Richest Customer Wealth
// https://leetcode.com/problems/richest-customer-wealth/

#include <vector>
#include <numeric>

using namespace std;


// O(m x n) time, O(1) space, where m is the number of customers and n is the number of accounts per customer
auto maximum_wealth(vector <vector<int>> &accounts) -> int {
  int result = 0;
  for (auto &account: accounts) {
    result = max(result, accumulate(account.begin(), account.end(), 0));
  }
  return result;
}
