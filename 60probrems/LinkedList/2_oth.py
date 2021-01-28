# not understand

# divmod: 商と余りを返す
class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0
        tail = head = ListNode(0)
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1+v2+carry, 10)
            tail.next = ListNode(val)
            tail = tail.next
        return head.next