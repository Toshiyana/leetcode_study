import itertools

class Solution:
    def permute(self, nums: [int]) -> [[int]]:
        return list(itertools.permutations(nums))


nums = [1,2,3]

obj = Solution()
print(obj.permute(nums))