# wrong answer

class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        nums = [0]
        result = []
        for _ in range(N-1):
            for num in nums:
                if num == 0:
                    result.append(0)
                    result.append(1)
                else: # num == 1
                    result.append(1)
                    result.append(0)
            nums = result
        return nums[K-1]

N = 2
K = 1
obj = Solution()
print(obj.kthGrammar(N, K))