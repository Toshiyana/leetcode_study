# 速度の違う２つのポインタを利用したバターン

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head: # leetcodeではtestcaseにnullを含む場合あり
            return False
        slow = head #一つ先のポインタへ
        fast = head.next #二つ先のポインタへ
        while slow != fast: # slowとfastが同じポインタを指さない場合
            if not fast or not fast.next: # fastとfastの次がnullの場合はlinked-listは終わっているのでnullを返す
                return False
            slow = slow.next
            fast = fast.next.next
        return True # slowとheadが同じノードに到達すればループ