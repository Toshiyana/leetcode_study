class Sample:
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        primeSet = {2,3,5,7,11,13,17,19,23,29}
        
        primes = 0
        for n in range(L, R+1):
            ones = bin(n).count('1')
            if ones in primeSet:
                primes += 1
        
        return primes  