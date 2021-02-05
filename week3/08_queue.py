# Queue는 왜 필요할까?
# 예) 주문이 들어왔을 때, 먼저 들어온 순서대로 처리할 때, 먼저 해야할 일을 저장하고 싶을때
# 1. 데이터 입출력이 잦음 - use Linked List
# 2. Queue는 시작과 끝의 노드를 전부 가지고 있어야 한다.
# -> 맨 앞에서 데이터를 pop, 맨 뒤에서 데이터를 enqueue　하기 때문에!

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    # head -> None <- tail
    # head ->//  3  //<- tail
    # head ->//  3 -> 4  //<- tail
    # head ->//  3 -> 4 -> 5  //<- tail
    #                            +6 (new_queue)
    # head ->//  3 -> 4 -> 5 ->       //<- tail    - new_queue.next = tail.next
    # head ->//  3 -> 4 -> 5 ->   6   //<- tail    - tail.next = new_qeueu
    def enqueue(self, value):  # tail(맨 뒤)에 추가
        new_queue = Node(value)
        if self.is_empty():
            self.head = new_queue
            self.tail = new_queue
            return
        self.tail.next = new_queue
        self.tail = new_queue
        return

    def dequeue(self):  # head(맨 앞)에서 빼기
        if self.is_empty():
            return "Queue is Empty"
        delete_head = self.head.data
        self.head = self.head.next
        return delete_head

    def peek(self):
        if self.is_empty():
            return "Queue is Empty"
        return self.head.data

    def is_empty(self):
        return self.head is None

queue = Queue()
print(queue.is_empty())
queue.enqueue(3)
print(queue.peek())
print(queue.is_empty())
queue.enqueue(4)
print(queue.peek())
queue.enqueue(5)
print(queue.peek())
print(queue.is_empty())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())