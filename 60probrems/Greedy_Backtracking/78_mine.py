from typing import List
import itertools

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        for i in range(len(nums)+1):
            for c in itertools.combinations(nums, i):
                result.append(list(c))
        
        return result

nums = [1,2,3]
obj = Solution()
print(obj.subsets(nums))