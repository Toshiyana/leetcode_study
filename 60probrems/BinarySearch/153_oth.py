# simple binary search

from typing import  List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l < r:
            mid = (l+r)//2
            # print("l, r, mid", l, r, mid)
            # print("nums", nums[l], nums[r], nums[mid])
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid # -1しない！(sortされてたらok?)
            # print("l, r", l, r)
            # print("nums", nums[l], nums[r])
        return nums[l]

if __name__ == '__main__':
    # nums = [3,4,5,1,2]
    # nums = [4,5,6,7,0,1,2]
    nums = [3,1,2]

    obj = Solution()
    print(obj.findMin(nums))