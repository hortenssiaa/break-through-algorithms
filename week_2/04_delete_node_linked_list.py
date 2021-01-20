class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None: # cur.next == None일 때 까 == next가 None이 아닐 때 까
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        cur = self.head
        count = 0
        while count < index:
            cur = cur.next
            count += 1
        return cur

    # 0                 1       2 ...
    # node    new_node   next_node
    # [5]               [12] -> [4] -> [9] -> ...
    #       -> [7] ->
    def add_node(self, index, value):
        # index가 0일때, index-1 = -1이 될 때를 고려!
        new_node = Node(value) # [7]
        if index == 0: # [7] -> [5] -> [12] ...
            new_node.next = self.head # [7] -> [5] ... 인것을 알고
            self.head = new_node # 그리고 나서야 head에 7을 지정한다. head -> [7] ...
            return 
        node = self.get_node(index-1)
        # index 2번째에 넣고싶다면, 2-1번째 노드까지를 node에 넣고 + 2에 새로운 노드 + 원래 2-1번째 노드 뒤의 모든 것 다시 붙이기
        next_node = node.next
        node.next = new_node
        new_node.next = next_node
        return

    def delete_node(self, index):
        # index == 0일때, index-1이 -1이 될 경우를 고려!
        # [5] -> [4] -> [3]
        # [4] -> [3]
        if index == 0: # 맨 첫번째를 삭제한다는 말
            self.head = self.head.next
        node = self.get_node(index-1)
        node.next = node.next.next

    def append2(self, value):
        # 제일 마지막, 즉 next = None인 것 다음에 추가해줘야함
        cur = self.head
        while cur is not None:
            cur = cur.next # 그 다음에 아무것도 없는, 즉 마지막 node에 와있음
        # cur이 마지막 노드니깐, 그 next를 지정해주면 됨
        cur.next = Node(value)
        return

    def printall(self):
        cur = self.head
        while cur is not None: # 현재 값이 있을 때 == 현재가 None이 아닐때
            print(cur.data)
            cur = cur.next


linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(4)
linked_list.append(9)
# print(linked_list.get_node(1).data) # -> 5를 들고 있는 노드를 반환해야 합니다!
linked_list.add_node(2, 7)
linked_list.print_all()

linked_list.delete_node(3)
linked_list.print_all()

