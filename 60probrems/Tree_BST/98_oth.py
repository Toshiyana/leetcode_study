# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        output = []
        self.inOrder(root, output)

        print(output)

        for i in range(1, len(output)):
            if output[i-1] >= output[i]:
                return False

        return True

    def inOrder(self, root, output):
        if not root:
            return
        self.inOrder(root.left, output)
        output.append(root.val)
        self.inOrder(root.right, output)

# data = [2,1,3]
tree = TreeNode(2)
tree.left = TreeNode(1)
tree.right  = TreeNode(3)

# tree = TreeNode(1)
# tree.left = TreeNode(1)

# tree = TreeNode(0)

# tree = TreeNode(0)
# tree.left = TreeNode(-1)

# data = [5,4,6,null,null,3,7]
tree = TreeNode(5)
tree.left = TreeNode(4)
tree.right  = TreeNode(6)
tree.right.left = TreeNode(3)
tree.right.right = TreeNode(7)

obj = Solution()
print(obj.isValidBST(tree))
