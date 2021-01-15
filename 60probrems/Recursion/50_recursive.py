# 参考：

class Solution:
    def myPow(self, x, n):
        # print(x, n)
        if not n:
            return 1
        if n < 0: # n is minus
            return 1 / self.myPow(x, -n)
        if n % 2: # n is odd
            return x * self.myPow(x, n-1)
        return self.myPow(x*x, n/2) # n is even

x = 2.00000
n = 10
obj = Solution()
print(obj.myPow(x, n))