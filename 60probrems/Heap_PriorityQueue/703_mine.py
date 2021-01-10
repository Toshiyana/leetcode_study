class KthLargest:

    def __init__(self, k: int, nums: [int]):
        self.k = k
        self.nums_list = nums

    def add(self, val: int) -> int:
        self.nums_list.append(val)
        self.nums_list.sort(reverse=True)
        return self.nums_list[self.k-1]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

obj = KthLargest(3, [4,5,8,2])
print(obj.add(3))
print(obj.add(5))
print(obj.add(10))
print(obj.add(9))
print(obj.add(4))