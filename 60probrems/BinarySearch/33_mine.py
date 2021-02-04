from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not target in nums:
            return -1
        else:
            return nums.index(target)

nums = [4,5,6,7,0,1,2]
target = 0

obj = Solution()
print(obj.search(nums, target))