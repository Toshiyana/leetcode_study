# BFS, correct

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = [root] if root else []
        result = []
        while queue:
            queue_level = []
            val_level = []
            for el in queue:
                val_level.append(el.val)
                if el.left:
                    queue_level.append(el.left)
                if el.right:
                    queue_level.append(el.right)

            queue = queue_level
            result.append(val_level)

        return result

node = TreeNode(3)
nl = TreeNode(9)
nr = TreeNode(20)
nrl = TreeNode(15)
nrr = TreeNode(7)

node.left = nl
node.right = nr
node.right.left = nrl
node.right.right = nrr

# node = TreeNode(1)
# nl = TreeNode(2)
# nr = TreeNode(3)
# nll = TreeNode(4)
# nlr = TreeNode(5)

# node.left = nl
# node.right = nr
# node.left.left = nll
# node.left.right = nlr

obj = Solution()
print(obj.levelOrder(node))