class Solution:
    def maxSubArray(self, nums: [int]) -> int:
        if not nums:
            return 0

        curSum = maxSum = nums[0]
        for num in nums[1:]:
            # print("num: {}, curSum+num: {} + {} = {}".format(num, curSum, num, curSum+num))
            curSum = max(num, curSum + num)
            # print("curSum:", curSum)

            # print("maxSum: {}, curSum: {}".format(maxSum, curSum))
            maxSum = max(maxSum, curSum)
            # print("maxSum:", maxSum)

            # print("")

        return maxSum


nums = [-2,1,-3,4,-1,2,1,-5,4]

obj = Solution()
print(obj.maxSubArray(nums))