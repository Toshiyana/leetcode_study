from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] == target:
                return mid
            
            if nums[l] <= nums[mid]: # l ~ mid間で昇順
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else: # nums[l] <= nums[mid] <= target
                    l = mid + 1
            else: # mid ~ r間で昇順（l ~ mid間で昇順出ない = rotateされてる）
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else: # target <= nums[mid] <= nums[r]:
                    r = mid - 1
        return -1

nums = [4,5,6,7,0,1,2]
target = 0

obj = Solution()
print(obj.search(nums, target))