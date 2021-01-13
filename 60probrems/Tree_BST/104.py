# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# BFS (Breadth First Search)
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        depth = 0
        level = [root] if root else []
        while level:
            depth += 1
            queue = []
            # print("depth:", depth)
            # print("level:", level)
            for el in level:
                # print("el:", vars(el))
                if el.left:
                    queue.append(el.left)
                if el.right:
                    queue.append(el.right)
                # print("")
            level = queue
            # print("---------------------")
        return depth


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