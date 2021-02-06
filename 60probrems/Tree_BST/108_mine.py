# wrong answer

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        mid = (len(nums)-1)//2
        head = tail = TreeNode(nums[mid])
        l = mid - 1
        r = mid + 1
        while l >= 0:
            tail.left = TreeNode(nums[l])
            tail = tail.left
            l -= 1

        tail = head
        while r <= len(nums)-1:
            tail.right = TreeNode(nums[r])
            tail = tail.right
            r += 1

        return head

arr = [-10,-3,0,5,9]
obj = Solution()
print(obj.sortedArrayToBST(arr))