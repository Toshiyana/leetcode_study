# Implementation based on O(1) aux space == almost the same as 122_oth2.py
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]):
        profit_from_price_gain = 0
        for idx in range(len(prices)-1):
            if prices[idx] < prices[idx+1]:
                profit_from_price_gain += prices[idx+1] - prices[idx]
        return profit_from_price_gain

data = [7,1,5,3,6,4]
# data = [1,2,3,4,5]
obj = Solution()
print(obj.maxProfit(data))