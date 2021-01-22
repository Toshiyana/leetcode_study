# wrong answer （おしいところまでいった）

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return

        # tail = head
        # while tail.next != None:
        #     if tail.val == tail.next.val and tail.next.next != None:
        #         tail.next = tail.next.next
        #     elif tail.val == tail.next.val and tail.next.next == None:
        #         tail.next = None
        #         return head

        #     tail = tail.next

        # return head

        tail = head
        while tail.next != None:
            if tail.val == tail.next.val:
                if tail.next.next != None:
                    if tail.next.next.val != tail.val:
                        tail.next = tail.next.next
                    else: # tail.next.next.val == tail.val:
                        tail.next = None
                        return head
                else: # tail.next.next == None:
                    tail.next = None
                    return head

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