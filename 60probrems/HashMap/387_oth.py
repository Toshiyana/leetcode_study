class Solution:
    def firstUniqChar(self, s: str) -> int:
        map = {}
        for i in s:
            if not i in map:
                map[i] = 1
            else:
                map[i] += 1

        for j in range(len(s)):
            if map[s[j]] == 1:
                return j
        return -1

# s = "leetcode"
# s = "aadadaad"
s = "loveleetcode"
obj = Solution()
print(obj.firstUniqChar(s))