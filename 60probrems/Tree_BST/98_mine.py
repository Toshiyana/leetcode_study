# wrong（二分木のルールを理解できていなかった）

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root.left and not root.right:
            return True
        # if not root.left or not root.right:
        #     return False

        queue = [root] if root else []

        while queue:
            queue_level = []
            for el in queue:
                if el.left:
                    if el.left.val < el.val:
                        queue_level.append(el.left)
                    else:
                        return False
                if el.right:
                    if el.right.val > el.val:
                        queue_level.append(el.right)
                    else:
                        return False
            queue = queue_level
        return True


# data = [2,1,3]
tree = TreeNode(2)
tree.left = TreeNode(1)
tree.right  = TreeNode(3)

# tree = TreeNode(1)
# tree.left = TreeNode(1)

# tree = TreeNode(0)

# tree = TreeNode(0)
# tree.left = TreeNode(-1)

data = [5,4,6,null,null,3,7]

obj = Solution()
print(obj.isValidBST(tree))