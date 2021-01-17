class Solution:
    def lengthOfLongestSubstring(self, s):
        start = maxLength = 0
        usedChar = {}

        for i, c in enumerate(s):
            if c in usedChar and start <= usedChar[c]:
                start = usedChar[c] + 1
            else:
                maxLength = max(maxLength, i - start + 1)

            usedChar[c] = i
        
            # print(usedChar)
            # print(maxLength)

        return maxLength

# s = "abcabcbb"
# s = "dvdf"
s = "anviaj"

obj = Solution()
print(obj.lengthOfLongestSubstring(s))