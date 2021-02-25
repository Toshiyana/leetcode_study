# Time Limit Exceeded, 出力は多分あっている
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if None in strs:
            return [[""]]

        list_map = []
        for s in strs:
            map = self.count_str(s)
            if not map in list_map:
                list_map.append(map)

        result = []
        for i in list_map:
            list_anagram = []
            for s in strs:
                map = self.count_str(s)
                if map == i:
                    list_anagram.append(s)
            result.append(list_anagram)

        return result
    
    def count_str(self, str):
        map = {}
        for c in str:
            if not c in map:
                map[c] = 1
            else:
                map[c] += 1
        return map