# wrong answer

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit, min_profit = 0, float('inf')
        for price in prices:
            min_profit = min(price, min_profit)
            profit = price - min_profit
            max_profit = max(profit, max_profit)

        return max_profit

data = [1,2,3,4,5]
obj = Solution()
print(obj.maxProfit(data))