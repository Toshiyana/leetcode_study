from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for w in strs:
            key = tuple(sorted(w))
            # d.get(key, []): keyが存在した場合valを返し，存在しない場合[]を返す
            d[key] = d.get(key, []) + [w]
        return list(d.values())

strs = ["eat","tea","tan","ate","nat","bat"]
# output = [["bat"],["nat","tan"],["ate","eat","tea"]]

# strs = ["ddddddddddg","dgggggggggg"]

obj = Solution()
print(obj.groupAnagrams(strs))