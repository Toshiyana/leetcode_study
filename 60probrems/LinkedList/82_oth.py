# 考えた人すごすぎ（デバッグで処理の流れを理解）

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head

        pre = dummy # set up pre and cur pointers
        cur = head
        while cur:
            if cur.next and cur.val == cur.next.val:
                while cur.next and cur.val == cur.next.val:
                    cur = cur.next
                # print(vars(cur))
                pre.next = cur.next # propose the next for pre
                                    # this will be verified by next line
                print("if", vars(pre.next))
                #print("")
            
            else: # if not cur.next or cur.val != cur.next.val
                pre = pre.next
                print("else",vars(pre))
            cur = cur.next
        return dummy.next

data = [1,2,3,3,4,4,5]
# data = [1,2,2]
tail = head = ListNode(data[0])
for i in data[1:]:
    tail.next = ListNode(i)
    tail = tail.next

# print(vars(head.next))

obj = Solution()
result = obj.deleteDuplicates(head)
print(vars(result))