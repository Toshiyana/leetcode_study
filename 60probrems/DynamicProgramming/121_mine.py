# Time Limit Exceeded, but maybe output is true.

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        for buy_day in range(len(prices)):
            buy_price = prices[buy_day]
            for sail_day in range(len(prices[buy_day:])):
                # print(buy_day, sail_day + buy_day)
                sail_price = prices[sail_day + buy_day]
                profit = sail_price - buy_price
                if profit > max_profit and sail_price > buy_price:
                    max_profit = profit
        
        return max_profit



prices = [7,1,5,3,6,4]
prices = [7,6,4,3,1]

obj = Solution()
print(obj.maxProfit(prices))
# print(prices[1:])