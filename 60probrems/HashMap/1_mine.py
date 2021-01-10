import itertools

class Solution:
    def twoSum(self, nums: [int], target: int):
        combi_two = itertools.permutations(nums,2) # 2つとり出す組み合わせ
        for i in combi_two:
            # print(i)
            if sum(i) == target:
                if i[0] == i[1]:
                    return self.my_index_multi(nums, i[0])
                else:
                    return [nums.index(i[0]), nums.index(i[1])] # numsの中で異なるindexの同じ値を選ぶ場合，list.index()だと最初の要素のindexを選んでしまう

    def my_index_multi(self, l, x): # list内の重複した要素について，値の異なるindexを取得
        return [i for i, _x in enumerate(l) if _x == x]

# nums = [2,7,11,15]
# target = 9

nums = [3,3]
target = 6

obj = Solution()
print(obj.twoSum(nums, target))