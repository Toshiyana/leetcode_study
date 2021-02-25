# wrong, 全て文字列が異なっていれば多分ok(今回の問題では，同じ文字列を含む場合もあるのでだめ)

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if None in strs:
            return [[""]]

        list_set = []
        for s in strs:
            set_s = set(s)
            if not set_s in list_set:
                list_set.append(set_s)

        result = []
        for i in list_set:
            list_anagram = []
            for s in strs:
                if set(s) == i:
                    list_anagram.append(s)
            result.append(list_anagram)

        return result

# strs = ["eat","tea","tan","ate","nat","bat"]
# output = [["bat"],["nat","tan"],["ate","eat","tea"]]

strs = ["ddddddddddg","dgggggggggg"]

obj = Solution()
print(obj.groupAnagrams(strs))