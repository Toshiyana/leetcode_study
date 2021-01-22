# My answer is correct, but not simple

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        stack = list()

        # stackに追加
        tail = head
        while tail:
            stack.append(tail.val)
            tail = tail.next

        # reverseしたオブジェクトを返す
        tail = head
        while tail:
            tail.val = stack.pop()
            tail = tail.next
        
        return head

data = [1,2,3,4,5]

head = tail = ListNode(data[0])
for i in data[1:]:
    tail.next = ListNode(i)
    tail = tail.next

obj = Solution()
result = obj.reverseList(head)
print(vars(result.next))