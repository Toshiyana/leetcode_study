# HashTable, HashSetを利用

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# # Table(辞書)を利用したパターン
# class Solution:
#     def hasCycle(self, head: ListNode) -> bool:
#         dictionary = {}
#         while head: # headにはlinksオブジェクトのアドレスが渡される
#             if head in dictionary:
#                 return True
#             else:
#                 dictionary[head]= True # Trueとする意味は特にない（下の集合に追加するやつの方がシンプル）
#                 print(dictionary)
#             head = head.next
#         return False

# set(集合)を利用したパターン
class Solution:
  def hasCycle(self, head):
    seen = set()
    curr = head
    # print(curr)
    while curr: # currがNoneでない限りループ
      if curr in seen:
        # print(curr)
        return True
      seen.add(curr)
      # print(seen)
      curr = curr.next
      # print(curr)
    return False


# head = [3,2,0,-4]
pos = 1 # posはパラメータではなく、最後の要素がどこに戻るかを示す。（この場合、最後の-4は１番目の要素の2に戻る）

# 循環ex
links = ListNode(3)
# print(vars(links))
links.next = ListNode(2)
# print(vars(links))
# print(vars(links.next))
links.next.next = ListNode(0)
# print(vars(links.next))
# print(vars(links.next.next))

links.next.next.next = ListNode(-4)
links.next.next.next.next = links.next # 2に戻る(循環させる)
# print(vars(links.next.next.next))
# print(vars(links.next.next.next.next)) # 循環を確認
# print(vars(links.next.next.next.next.next))

obj = Solution()
print(obj.hasCycle(links))