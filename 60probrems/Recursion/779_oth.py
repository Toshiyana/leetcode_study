# not understand

class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        if N == 1: # Base Case
            return 0
        else: # General Case
            if K % 2 == 0:
                # even index of current level is opposite of parent level's [(K+1)//2]
                return 0 if self.kthGrammar(N-1, (K+1)//2) else 1
            else:
                # odd index of current level is the same as parent level's [(K+1)//2]
                return 1 if self.kthGrammar(N-1, (K+1)//2) else 0
