# res and DFS

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        res = []
        self.dfs(root, targetSum, res)
        return any(res)
    
    def dfs(self, root, target, res):
        if root:
            if not root.left and not root.right and root.val == target:
                res.append(True)
            if root.left:
                self.dfs(root.left, target-root.val, res)
            if root.right:
                self.dfs(root.right, target-root.val, res)