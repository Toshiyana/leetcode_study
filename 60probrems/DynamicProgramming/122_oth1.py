# Implementation by DP

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # It is impossible to sell stock on first day, set -infinity as initial value for cur_hold
        cur_hold, cur_not_hold = -float('inf'), 0
        for stock_price in prices:
            prev_hold, prev_not_hold = cur_hold, cur_not_hold

            # either keep hold, or buy in stock today at stock price
            cur_hold = max(prev_hold, prev_not_hold - stock_price)# 株を持ってる状態（０から株を買ってマイナスの状態 or 得た利益-買う株価）

            # either keep not-hold, or sell out stock today at stock price
            cur_not_hold = max(prev_not_hold, prev_hold + stock_price)# 株を持ってない状態（利益が出た状態(または何もない) or 株を持ってる状態+売る株価）

        # maximum profit must be in not-hold state
        return cur_not_hold if prices else 0

data = [7,1,5,3,6,4]
# data = [1,2,3,4,5]
obj = Solution()
print(obj.maxProfit(data))