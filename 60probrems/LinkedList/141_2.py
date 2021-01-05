# 速度の違う２つのポインタを利用したバターン

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head: # leetcodeではtestcaseにnullを含む場合あり
            return False
        slow = head #一つ先のポインタへ
        fast = head.next #二つ先のポインタへ
        # print(slow, fast)
        while slow != fast: # slowとfastが同じアドレスを指さない限りループ（循環していれば、速度の違うslowとfastはいずれ同じアドレスを指す）
            if not fast or not fast.next: # fastとfastの次がnullの場合はlinked-listは終わっているのでFalseを返す
                return False
            slow = slow.next
            fast = fast.next.next
            print(slow, fast) # slowとfastの遷移を確認
        return True # slowとheadが同じノードに到達すればループ

# data = [3,2,0,-4]
# pos = 1 # posはパラメータではなく、最後の要素がどこに戻るかを示す。（この場合、最後の-4は１番目の要素の2に戻る）

# 循環する連結リストの作成方法１
links = ListNode(3)
# print(vars(links))
links.next = ListNode(2)
# print(vars(links))
# print(vars(links.next))
links.next.next = ListNode(0)
# print(vars(links.next))
# print(vars(links.next.next))

links.next.next.next = ListNode(-4)
links.next.next.next.next = links.next # 2に戻る(循環させる)
# print(vars(links.next.next.next))
# print(vars(links.next.next.next.next)) # 循環を確認
# print(vars(links.next.next.next.next.next))

# 最初のslowとfastのアドレスがそれぞれlinksとlinks.nextに一致するか確認
# print(links)
# print(links.next)


# 循環する連結リストの作成方法2
data = [3,2,0,-4]
# pos = 1 # posはパラメータではなく、最後の要素がどこに戻るかを示す。（この場合、最後の-4は１番目の要素の2に戻る）

# ループで連結リストを作成
tail = head = ListNode(data[0])
for i in data[1:]:
    tail.next = ListNode(i) # アドレスは１回目でhead.next、２回目でhead.next.next,3回目でhead.next.next.next
    tail = tail.next

head.next.next.next.next = head.next

# # 確認
# print(vars(head))
# print(vars(head.next))
# print(vars(head.next.next))
# print(vars(head.next.next.next))
# print(vars(head.next.next.next.next))

obj = Solution()
# print(obj.hasCycle(links))
print(obj.hasCycle(head))

# 遷移の確認
# slow(一個一個進む)：3,2,0,-4
# fast（一つとばし）: 2,-4,0 (2,-4,0でループより)
# よって、slowとfastは２回の遷移で同じ０のアドレスになり、循環を確認