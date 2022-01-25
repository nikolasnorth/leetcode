// 134. Gas Station
// https://leetcode.com/problems/gas-station/

#include <vector>
#include <numeric>

using namespace std;


// O(n) time, O(1) space, where n is the size of `gas`
auto can_complete_circuit(vector<int> &gas, vector<int> &cost) -> int {
  if (accumulate(gas.begin(), gas.end(), 0) < accumulate(cost.begin(), cost.end(), 0)) {
    return -1;
  }
  int tank = 0, start = 0;
  for (int i = 0; i < gas.size(); ++i) {
    tank += gas[i] - cost[i];
    if (tank < 0) {
      tank = 0;
      start = i + i;
    }
  }
  return start;
}
