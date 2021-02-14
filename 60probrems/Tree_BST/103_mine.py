# correct
# Runtime: 24ms
# Memory: 14.3MB
from typing import List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = [root] if root else []
        result = []
        level = 0
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
            if level%2 == 0:
                result.append(val_level)
            else:
                # val_level.reverse() # val_level[::-1]と同じ反転処理
                result.append(val_level[::-1])
            level += 1

        return result
