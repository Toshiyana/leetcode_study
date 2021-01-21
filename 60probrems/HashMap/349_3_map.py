# use dict/hashmap to record all nums appeared in the first list, and then check if there are nums in the second list have appeared in the map.

class Solution:
    def intersection(self, nums1: [int], nums2: [int]) -> [int]:
        res = []
        map = {}

        for i in nums1:
            map[i] = map[i] + 1 if i in map else 1
        for j in nums2:
            if j in map and map[j] > 0:
                res.append(j)
                map[j] = 0
                
        return res

# nums1 = [1,2,2,1]
# nums2 = [2,2]

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

obj = Solution()
print(obj.intersection(nums1, nums2))