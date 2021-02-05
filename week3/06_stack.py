# stack : 데이터 입출력이 잦음 - use Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        cur = self.head
        if cur is None:
            self.head = Node(value)
            return
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    # pop 기능 구현
    def pop(self):
        cur = self.head
        while cur.next is not None:
            if cur.next.next is None:
                data = cur.next.data
                cur.next = None
                return data
            cur = cur.next
        data = cur.data
        self.head = None
        return data

    def peek(self):
        cur = self.head
        if cur is None:
            return None
        while cur.next is not None:
            cur = cur.next
        return cur.data

    # isEmpty 기능 구현
    def is_empty(self):
        cur = self.head
        if cur is None:
            return True
        else:
            return False

stack1 = Stack()
print(stack1.is_empty())
stack1.push(5)
print(stack1.peek())
print(stack1.is_empty())
stack1.push(4)
stack1.push(8)
print(stack1.peek())
print(stack1.pop())
print(stack1.pop())
print(stack1.is_empty())
print(stack1.pop())
print(stack1.is_empty())
print(stack1.peek())
