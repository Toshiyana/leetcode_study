# correct answer

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        tail = head
        while tail:
            while tail.next and tail.val == tail.next.val:
                tail.next = tail.next.next # skip duplicated nodes(Noneが入る可能性有り)
            tail = tail.next

        return head


# links = [1, 1, 2]
# links = [1, 1, 2, 3, 3]
# links = [1, 1, 1]
links = [1, 1, 1, 2] # 連続して同じ値が出た後に，異なる値が出るテストケースの解決方法が分からない


head = tail = ListNode(links[0])
for i in links[1:]:
    tail.next = ListNode(i)
    tail = tail.next

obj = Solution()
print(vars(obj.deleteDuplicates(head).next))