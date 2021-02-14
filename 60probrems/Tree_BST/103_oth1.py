# Runtime: 32ms
# Memory: 14.6MB

from typing import List
import collections

# collectionsモジュールとは:
# 標準ライブラリcollectionsモジュールのdeque型を使うと、
# データをキューやスタック、デック（両端キュー）として効率的に扱える

# 利点：
# 標準のリストをキューやスタック，デック（両端キュー）として使うよりも，
# deque型の方が処理速度が速い（リストは先頭の要素に対する削除や挿入の処理速度が遅いため）

# 欠点：
# 両端以外の要素へのアクセスは遅い

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = collections.deque([root])
        res = []
        while queue:
            r = []
            for _ in range(len(queue)):
                q = queue.popleft()
                if q:
                    r.append(q.val)
                    queue.append(q.left)
                    queue.append(q.right)
            r = r[::-1] if len(res) % 2 else r # 反転処理
            if r:
                res.append(r)
        return res