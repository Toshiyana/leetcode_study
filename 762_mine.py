# 762. Prime Number of Set Bits in Binary Representation
# collect!
class Solution:
    def countPrimeSetBits(self, L: int, R: int):
        def isPrime(n):
            if n==2 or n==3: return True
            if n%2 == 0 or n<2: return False
            for i in range(3,int(n**0.5)+1,2): #only odd
                if n%i == 0:
                    return False
            return True
        
        count_prime = 0
        for i in range(L,R+1):
            count_bits = bin(i).count('1')
            if isPrime(count_bits) == True:
                count_prime += 1
                
        return count_prime

obj = Solution()
print(obj.countPrimeSetBits(249,269))