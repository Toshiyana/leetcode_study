# 片方向リストの理解（ノードを一番後ろに接続する場合）
# 参考：https://astrostory.hatenablog.com/entry/2020/02/24/070213

class LinkedList:
  class Node:
    def __init__(self, payload):
      self.payload = payload
      self.next = None
  
  def __init__(self):
    self.head = None

  def addNode(self, newpayload):
    newnode = LinkedList.Node(newpayload)
    if self.head == None:
      self.head = newnode
      return

    else: # 最後のノードに連結する場合
      runner = self.head # runnnerをheadとする
      # runnnerにheadのアドレスが渡される(headの中身は変わらない)
      # print("runner: {}".format(vars(runner)))
      while runner.next != None: # runnerがNoneのところに行くまでタスキを回すイメージ
        # runnerは次のノードに別のノードが接続されないノードになるまで移動（連結リストの最後）
        runner = runner.next # headをずらす（headにnextのオブジェクトが入る）
        # runnnerにhead.nextのアドレスが渡される
        # print("runner2: {}".format(vars(runner)))
      
      # runnnerが最後のノードに移った後、最後のノードの次のruuner.nextに新しいノードを代入
      runner.next = newnode
      # runner.next(=head.next.next)にオブジェクトを渡す
      # 参照元も書き換わる

# headはまだ空の状態
links = LinkedList()
print(vars(links))
#print(links) # object at 0x~は16進数
print("links:",id(links)) # idは上の16進数を10進数に変換したもの
#print(links.head)
print("head:",id(links.head))
print("")

# headにnode（payload:26, next:none）を追加
links.addNode(26)
print(vars(links.head)) # オブジェクトの中身を取得
# print(dir(links.head)) # メソッド名や値を取得
#print(links.head)
print("head:",id(links.head)) # 新しく生成されたオブジェクトのidが入るため、上の空の時のアドレスとは異なる
print("payload:{}, next:{}".format(id(links.head.payload), id(links.head.next))) # 上のid(links.head)のアドレスが入る
# 最後のノードの次の部分が、一番最初のheadのアドレスになる？
print("")

# head.nextにnode（payload:99, next:none）を追加
links.addNode(99)
print(vars(links.head)) # オブジェクトの中身を取得
print(vars(links.head.next))
print("head:",id(links.head)) #最初にオブジェクトが生成されて以降、headのidは変わらない
print("payload:{}, next:{}".format(id(links.head.payload), id(links.head.next))) # 上のid(links.head)のアドレスが入る
print("head.next.payload:{}, head.next.next:{}".format(id(links.head.next.payload), id(links.head.next.next)))
print("")

# head.nextにnode（payload:99, next:none）を追加
links.addNode(127)
print(vars(links.head)) # オブジェクトの中身を取得
print(vars(links.head.next))
print(vars(links.head.next.next))
print(id(links.head))
print(id(links.head.next))
print(id(links.head.next.next))
print(id(links.head.next.next.next))
print("")