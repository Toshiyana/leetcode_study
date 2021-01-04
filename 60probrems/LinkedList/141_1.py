# HashSet（辞書）を利用

# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 辞書を利用したパターン
# class Solution:
#     def hasCycle(self, head: ListNode) -> bool:
#         dictionary = {}
#         while head:
#             if head in dictionary: 
#                 return True
#             else: 
#                 dictionary[head]= True
#             head = head.next
#         return False

# 集合を利用したパターン
class Solution:
  def hasCycle(self, head):
    seen = set()
    curr = head
    while curr:
      if curr in seen:
        return True
      seen.add(curr)
      curr = curr.next
    return False


head = ListNode([3,2,0,-4])
pos = 1

obj = Solution()
print(obj.hasCycle(head))