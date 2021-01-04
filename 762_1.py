class Solution:
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        def isPrime(n):
            if n==2 or n==3: return True
            if n%2==0 or n<2: return False
            for i in range(3,int(n**0.5)+1,2):   # only odd numbers
                if n%i==0:
                    return False    

            return True
        
        def countOnes(n):
            ones = 0
            while n:
                check = 1
                check &= n
                ones += check
                n >>= 1
            
            return ones
        
        primes = 0
        for n in range(L, R+1):
            ones = countOnes(n)
            if isPrime(ones):
                primes += 1
        
        return primes  