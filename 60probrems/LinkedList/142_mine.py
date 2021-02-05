# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# class Solution:
#     def detectCycle(self, head: ListNode) -> ListNode:
#         seen = []
#         curr = head
#         while curr:
#             if curr in seen:
#                 return "tail connects to node index " + str(seen.index(curr))
#             seen.append(curr)
#             curr = curr.next
#         return "no cycle"

# # My answer is correct(use list：超遅いからだめ 884ms)
# class Solution:
#     def detectCycle(self, head: ListNode) -> ListNode:
#         seen = []
#         curr = head
#         while curr:
#             if curr in seen:
#                 return curr
#             seen.append(curr)
#             curr = curr.next
#         return

# My answer is correct(use set：早い 44ms，setは順序や位置を記憶しないので早い（後から追加したものが後に入ってるとは限らない）．)
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        seen = set()
        curr = head
        while curr:
            if curr in seen:
                return curr
            seen.add(curr)
            curr = curr.next
        return

data = [3,2,0,-4]
pos = 1
head = tail = ListNode(data[0])
for i in data[1:]:
    tail.next = ListNode(i)
    tail = tail.next

head.next.next.next.next = head.next
# print(vars(head.next.next.next.next))

obj = Solution()
print(obj.detectCycle(head))