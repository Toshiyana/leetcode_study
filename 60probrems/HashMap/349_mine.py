class Solution:
    def intersection(self, nums1: [int], nums2: [int]) -> [int]:
        len_1 = len(nums1)
        len_2 = len(nums2)
        list = []

        if len_1 < len_2:
            nums_for = nums1
            nums_oth = nums2
        else:
            nums_for = nums2
            nums_oth = nums1

        for i in nums_for:
            if i in nums_oth and not i in list:
                list.append(i)

        return list

# nums1 = [1,2,2,1]
# nums2 = [2,2]

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

obj = Solution()
print(obj.intersection(nums1, nums2))