class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def get_kth_node_from_last(self, k): # 뒤에서 k번째 노드까지 이동
        count_node = 1
        cur = self.head

        while cur.next is not None:
            cur = cur.next # 마지막까지 갔으면
            count_node += 1

        # print(count_node)
        # k==1; 맨 뒤 cur, k==2; 맨 뒤에서 하나 앞
        cur = self.head
        if count_node - k < 0:
            return

        for go_kth in range(count_node - k): # range(n) : 0부터 n까지 즉, n-1번 반복해라
            cur = cur.next
        return cur

    def get_head_data(self):
        cur = self.head
        return cur


linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)
# 6 -> 7 -> 8
print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!
# print(linked_list.get_head_data().data)
