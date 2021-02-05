class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    # head     tail
    # [4]  ->  [2]
    # new_node = Node(3)

    # head    tail
    #  [4] -> [2] -> [3]
    # self.tail.next = new_node

    # head           tail
    #  [4] -> [2] -> [3]
    # self.tail = new_node
    def enqueue(self, value):  # tail(맨 뒤)에 추가
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node
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