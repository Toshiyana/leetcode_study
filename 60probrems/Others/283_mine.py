# two-pointers, inplace
class Solution:
    def moveZeroes(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = 0 # records the position of "0"
        for i in range(len(nums)):
            if nums[i] != 0:
                print("nums[{}], nums[{}] = nums[{}], nums[{}] = {}, {}".format(i, zero, zero, i, nums[zero], nums[i]))
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1
        
        # print(nums)

input = [0,1,0,3,12]
output = [1,3,12,0,0]

obj = Solution()
obj.moveZeroes(input)