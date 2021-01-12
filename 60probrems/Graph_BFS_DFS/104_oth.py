# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # print(vars(root))
        print(1 + max(self.maxDepth(root.left), self.maxDepth(root.right)) if root else 0)
        print("")
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right)) if root else 0

root = [3,9,20,None,None,15,7]
t = TreeNode(3)
tl = TreeNode(9)
tr = TreeNode(20)
trl = TreeNode(15)
trr = TreeNode(7)

t.left = tl
t.right = tr
tr.left = trl
tr.right = trr

# print(vars(t))
# print(vars(t.left))
# print(vars(t.right))
obj = Solution()
print(obj.maxDepth(t))