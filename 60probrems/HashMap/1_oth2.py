class Solution:
    # @return a tuple, (index1, index2)
    # 8:42
    def twoSum(self, nums, target):
        map = {}
        for i in range(len(nums)):
            if nums[i] not in map:
                map[target - nums[i]] = i # {差分の値（次この値が出れば終了）：今の値のindex}
                print(map)
            else:
                return map[nums[i]], i

        return -1, -1

# nums = [2,7,11,15]
# target = 9

nums = [2,11,7,15]
target = 9

# nums = [3,3]
# target = 6

obj = Solution()
print(obj.twoSum(nums, target))