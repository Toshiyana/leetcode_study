# wrong answer
from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        string = s
        for dic in wordDict:
            while dic in string:
                # delete dic from s
                string = string.replace(dic, '')
        if not string:
            return True
        else:
            return False

s = "applepenapple"
wordDict = ["apple", "pen"]

obj = Solution()
print(obj.wordBreak(s, wordDict))