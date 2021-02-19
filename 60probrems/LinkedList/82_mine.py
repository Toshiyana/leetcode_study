# wrong answer : 惜しいところまでいってる．重複した時に，最後の要素が0になっちゃう．

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None
        
        dic = {}
        tail = head
        while tail:
            if not tail.val in dic:
                dic[tail.val] = 1
            else:
                dic[tail.val] += 1
            tail = tail.next
        
        # print(dic)
        
        tail = head
        tail_out = head_out = ListNode()
        while tail:
            if dic[tail.val] == 1:
                tail_out.val = tail.val
                if tail.next:
                    tail_out.next = ListNode()
                    tail_out = tail_out.next                        
            tail = tail.next
        
        if head_out.val == 0:
            return None
        else:
            return head_out

# data = [1,2,3,3,4,4,5]
data = [1,2,2]
tail = head = ListNode(data[0])
for i in data[1:]:
    tail.next = ListNode(i)
    tail = tail.next

# print(vars(head.next))

obj = Solution()
result = obj.deleteDuplicates(head)
print(vars(result))