# 理解しきれてない
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head, prev = None) -> ListNode:

        if not head:
            return prev

        next = head.next
        head.next = prev

        return self.reverseList(next, head)

data = [1,2,3,4,5]

head = tail = ListNode(data[0])
for i in data[1:]:
    tail.next = ListNode(i)
    tail = tail.next

obj = Solution()
result = obj.reverseList(head)
print(vars(result.next))