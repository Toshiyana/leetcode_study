class Solution:
    def lengthOfLongestSubstring(self, s):
        start = maxLength = 0
        usedChar = {}

        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)

            usedChar[s[i]] = i
        
            # print(usedChar)
            # print(maxLength)

        return maxLength

# s = "abcabcbb"
# s = "dvdf"
s = "anviaj"

obj = Solution()
print(obj.lengthOfLongestSubstring(s))