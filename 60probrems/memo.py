class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

head = ListNode([3,2,0,-4])
seen = set()
seen.add(head)
print(seen)

# nodeSeen = {}
# while head is not None:
#   if head in nodeSeen:
#     return True