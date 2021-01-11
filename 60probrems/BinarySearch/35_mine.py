class Solution:
    def searchInsert(self, nums: [int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l+r)//2
            # print('before:',l,r,mid)

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

            # print('after:',l,r,mid)
        return l

# nums = [1,3,5,6]
# target = 5

nums = [1,3,5,6]
target = 2

obj = Solution()
print(obj.searchInsert(nums, target))