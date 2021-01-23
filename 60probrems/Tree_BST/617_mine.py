# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 and t2:
            root = TreeNode(t1.val + t2.val)
            root.left = self.mergeTrees(t1.left, t2.left)
            root.right = self.mergeTrees(t1.right, t2.right)
            return root
        else:
            return t1 or t2

node1_1 = TreeNode(1)
node1_2 = TreeNode(3)
node1_3 = TreeNode(2)
node1_4 = TreeNode(5)

node1_1.left = node1_2
node1_2.left = node1_4
node1_1.right = node1_3

node2_1 = TreeNode(2)
node2_2 = TreeNode(1)
node2_3 = TreeNode(3)
node2_4 = TreeNode(4)
node2_5 = TreeNode(7)

node2_1.left = node2_2
node2_2.right = node2_4
node2_1.right = node2_3
node2_3.right = node2_5


obj = Solution()
print(vars(obj.mergeTrees(node1_1, node2_1)))