# 参考：https://qiita.com/maebaru/items/53a30c78bad8d0df92af#:~:text=%E6%B7%B1%E3%81%95%E5%84%AA%E5%85%88%E6%8E%A2%E7%B4%A2%20(Depth,%E3%81%99%E3%82%8B%E3%81%93%E3%81%A8%E3%81%8C%E3%81%A7%E3%81%8D%E3%81%BE%E3%81%99%E3%80%82

# DFS: stack or 再帰を使って実装（以下は再帰）

# Make tree as follows:
#     1
#    / \
#   2   5
#  / \ / \
# 3  4 6  7

class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)

node1.left = node2
node1.right = node5
node2.left = node3
node2.right = node4
node5.left = node6
node5.right = node7

def traverse(node):
    if node is not None:
        print(node.val)
        # 子要素に対して再帰的に呼び出していく
        traverse(node.left)
        traverse(node.right)

traverse(node1)