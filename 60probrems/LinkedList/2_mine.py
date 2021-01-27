# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        list1 = []
        list2 = []

        tail = l1
        while tail:
            list1.append(str(tail.val))
            tail = tail.next

        tail = l2
        while tail:
            list2.append(str(tail.val))
            tail = tail.next

        num1 = int(''.join(list(reversed(list1))))
        num2 = int(''.join(list(reversed(list2))))

        ans = str(num1 + num2)
        ans = list(ans)

        tail = head = ListNode(int(ans.pop(-1))) # intなくても正解だった（time: intなし（str）のときは80ms, intありの時は100ms）
        while ans:
            tail.next = ListNode(int(ans.pop(-1)))
            tail = tail.next

        return head