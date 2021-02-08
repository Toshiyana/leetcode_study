# Implementation based on list and sum()
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]):
        price_gain = []

        for idx in range(len(prices)-1):
            if prices[idx] < prices[idx + 1]:
                price_gain.append(prices[idx+1] - prices[idx])
        return sum(price_gain)

data = [7,1,5,3,6,4]
# data = [1,2,3,4,5]
obj = Solution()
print(obj.maxProfit(data))