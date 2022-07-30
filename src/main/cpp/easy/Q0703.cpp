#include <functional>
#include <queue>

using namespace std;

class KthLargest {
 private:
  int k_;
  priority_queue<int, vector<int>, greater<>> pq_;

 public:
  KthLargest(int k, vector<int>& nums)
      : k_(k), pq_(nums.begin(), nums.end(), greater<>()) {
    // We need to keep at most k elements. The top will be the k-th largest.
    while (pq_.size() > k_) pq_.pop();
  }

  int add(int val) {
    pq_.push(val);
    if (pq_.size() > k_) pq_.pop();
    return pq_.top();
  }
};
