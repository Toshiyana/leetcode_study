# This is same solution as mine.

# brute-force searching, search each element of the first list in the second list. (to be more efficient, you can sort the second list and use binary search to accelerate)

class Solution:
    def intersection(self, nums1: [int], nums2: [int]) -> [int]:
        res = []
        for i in nums1:
            if i not in res and i in nums2:
                res.append(i)
        
        return res

# nums1 = [1,2,2,1]
# nums2 = [2,2]

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

obj = Solution()
print(obj.intersection(nums1, nums2))