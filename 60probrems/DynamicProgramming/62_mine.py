import math
# combination
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if not m or not n:
            return 0
        return self.combinations_count(m-1, n-1)

    def combinations_count(self, a, b):
        return math.factorial(a+b) // (math.factorial(a) * math.factorial(b))

m, n = 3, 7
obj = Solution()
print(obj.uniquePaths(m,n))