# 理解しきれてない

# simple answer
# The idea is to change next with prev, prev with current, and current with next.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head

        while curr:
            next = curr.next # nextにcurr.nextのアドレスを代入（currはどんどん次へ）
            curr.next = prev # curr.nextにprevを代入（最初はNone）
            prev = curr # prevにcurrを代入（最初は{1, None}）
            curr = next # 更新

            # print(vars(prev))
        
        return prev

data = [1,2,3,4,5]

head = tail = ListNode(data[0])
for i in data[1:]:
    tail.next = ListNode(i)
    tail = tail.next

obj = Solution()
result = obj.reverseList(head)
print(vars(result.next))