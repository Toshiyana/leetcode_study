# 参考：https://qiita.com/b1ueskydragon/items/0b8e0c382d782423c6d3

class Solution:
    def myPow(self, x, n):
        if n < 0:
            x = 1 / x
            n = -n
        pow = 1
        while n:
            if n % 2: # == n & 1 == n is odd
                pow *= x
            x *= x
            n //= 2 # == n >>= 1
        return pow

x = 2.00000
n = 10
obj = Solution()
print(obj.myPow(x, n))