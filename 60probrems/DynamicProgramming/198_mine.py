# wrong answer

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return None
        
        length = len(nums)
        sum_fromZero = 0
        sum_fromOne = 0

        # 最大値となる時が，一個間隔とは限らないので，この方法はだめ
        for i in range(0, len(nums), 2):
            sum_fromZero += nums[i]
            if i+1 < length:
                sum_fromOne += nums[i+1]

        max_sum = max(sum_fromZero, sum_fromOne)
        return max_sum

nums = [1,2,3,1]
obj = Solution()
print(obj.rob(nums))
