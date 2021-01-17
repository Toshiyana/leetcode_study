# wrong answer

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not str:
            return 0
        list = []
        count = 0
        count_max = 0

        for i in range(len(s)):
            print(list)
            if not list:
                list.append(s[i])
                count += 1
                count_max = max(count, count_max)
            elif s[i] in list:
                if list[-1] == s[i]:
                    list = []
                    list.append(s[i])
                    count = 1
                    count_max = max(count, count_max)
                elif list[-1] != s[i]:
                    list = [list[-1]]
                    list.append(s[i])
                    count = 2
                    count_max = max(count, count_max)
            elif not s[i] in list:
                list.append(s[i])
                count += 1
                count_max = max(count, count_max)
        return count_max


# s = "abcabcbb"
# s = "dvdf"
s = "anviaj"

obj = Solution()
print(obj.lengthOfLongestSubstring(s))