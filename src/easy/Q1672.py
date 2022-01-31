"""
1672. Richest Customer Wealth
https://leetcode.com/problems/richest-customer-wealth/
"""
from typing import List


# O(m x n) time, O(1) space, where m is the number of customers and n is the number of accounts per customer
def maximum_wealth(accounts: List[List[int]]):
    result = 0
    for customer in accounts:
        result = max(result, sum(customer))
    return result
