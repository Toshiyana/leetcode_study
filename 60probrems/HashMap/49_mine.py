from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if None in strs:
            return [[""]]
        
        # stack = []
        # for s in strs:
        #     stack.append(set(s))
        
        # list_anagram = []
        # result = []
        # comp = stack[0]
        # # while stack:
        # #     list_anagram = []
        # for idx, set_str in enumerate(stack[1:]):
        #     print(idx+1, set_str)
        

        # result.append(list_anagram)

        # map = {}
        # for i in range(len(strs)):
        #     map[i] = set(strs[i])
        
        # print(map)

        list_set = []
        for s in strs:
            set_s = set(s)
            if not set_s in list_set:
                list_set.append(set_s)
        # print(list_set)

        result = []
        while strs:
            for i in list_set:
                list_anagram = []
                for s in strs:
                    print(s)
                    # print(set(s))
                    if set(s) == i:
                        list_anagram.append(s)
                        strs.remove(s)
                result.append(list_anagram)

        return result

strs = ["eat","tea","tan","ate","nat","bat"]
# output = [["bat"],["nat","tan"],["ate","eat","tea"]]

obj = Solution()
print(obj.groupAnagrams(strs))