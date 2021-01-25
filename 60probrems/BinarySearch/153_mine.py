from typing import  List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        return min(nums)

if __name__ == '__main__':
    nums = [3,4,5,1,2]

    print(min(nums))

    # obj = Solution()
    # print(obj.findMin())