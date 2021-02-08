class Solution:
    def firstUniqChar(self, s: str) -> int:
        map = {}
        min_idx = float('inf')
        flag = 0
        for i in range(len(s)):
            if not s[i] in map:
                map[s[i]] = i
            else:
                map[s[i]] = None

        for v in map.values():
            if v != None:
                flag = 1
                min_idx = min(min_idx, v)
        
        if not flag:
            return -1
        else:
            return min_idx

s = "leetcode"
#s = "aadadaad"
# s = "loveleetcode"
obj = Solution()
print(obj.firstUniqChar(s))