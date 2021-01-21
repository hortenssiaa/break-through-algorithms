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


def get_linked_list_sum(linked_list_1, linked_list_2):
    cur_ll1 = linked_list_1.head
    num_store1 = str(cur_ll1.data) # index가 0밖에 존재하지 않을 때

    cur_ll2 = linked_list_2.head
    num_store2 = str(cur_ll2.data) # index가 0밖에 존재하지 않을 때

    # while문은 1번 index 이상 존재할 때 실행
    while cur_ll1.next is not None: # cur_ll1이 마지막일 때까지 == 그러면 cur_ll1.next는 다음이니깐 없는 거겠지 (None)
        cur_ll1 = cur_ll1.next # 1번째 index 부터
        num_store1 += str(cur_ll1.data)

    while cur_ll2.next is not None:
        cur_ll2 = cur_ll2.next
        num_store2 += str(cur_ll2.data)

    return int(num_store1) + int(num_store2)


# [6] -> [7] -> [8]
linked_list_1 = LinkedList(6)
linked_list_1.append(7)
linked_list_1.append(8)

# [3] -> [5] -> [4]
linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)

print(get_linked_list_sum(linked_list_1, linked_list_2))