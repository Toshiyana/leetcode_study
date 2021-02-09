# DFS with Stack（Stack: 後に入れたものを先に取り出す）

class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        stack = [(root, root.val)]
        while stack:
            curr, val = stack.pop()
            if not curr.left and not curr.right and val == targetSum:
                return True
            if curr.right:
                stack.append((curr.right, val + curr.right.val))
            if curr.left:
                stack.append((curr.left, val + curr.left.val))
        return False