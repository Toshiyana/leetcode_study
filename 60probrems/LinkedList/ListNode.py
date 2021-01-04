# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

data = [5, 1, 7, 96]
tail = head = ListNode(data[0])

for x in data[1:]:
    tail.next = ListNode(x) # Create and add another node
    tail = tail.next # Move the tail pointer
    print(tail)