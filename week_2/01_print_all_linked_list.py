class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node = Node(3)

first_node = Node(4)
node.next = first_node
# print(node.data, node.next.data)
# print(first_node.data, first_node.next)


# linked list : 헤드 노드만 갖고 있으면 된다.
class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    def append(self, data):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(data)
        # print(cur.data)
        # head data : 3이고 next : Node 일 때, append(4) 하면, cur이 head라서 3 출력된다.

    def print_all(self):
        cur = self.head # 값이 있는 Node를 가리키는 포인터
        while cur is not None: # cur이 None 이다 == 아예 값이 있는 Node가 없다.
            print(cur.data)
            cur = cur.next

#  cur
# [3] -> [4] -> [5] -> None
linked_list = LinkedList(3)
linked_list.append(4)
linked_list.append(5)
linked_list.print_all()