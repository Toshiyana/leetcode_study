# collect

from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        result = []
        for i in nums:
            if not i in dic:
                dic[i] = 1
            else:
                dic[i] += 1

        for i in range(k):
            res_key = self.get_key(dic, max(dic.values()))
            result.append(res_key)
            dic.pop(res_key)
        
        return result

    def get_key(self, my_dict, val):
        for key, value in my_dict.items():
            if val == value:
                return key

# Runtime: 164 ms
# Memory Usage 18.6 MB

nums = [1,1,1,2,2,3]
k = 2
obj = Solution()
print(obj.topKFrequent(nums, k))