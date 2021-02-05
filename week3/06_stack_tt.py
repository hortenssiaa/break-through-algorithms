# stack : 데이터 입출력이 잦음 - use Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# head
#  5
# head
#  3   ->   5

class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        new_head = Node(value)
        new_head.next = self.head # 3 -> 5 가 되는거지
        self.head = new_head

    # pop 기능 구현
    def pop(self):
        if self.is_empty():
            return "Stack is Empty."
        delete_head = self.head.data
        self.head = self.head.next
        return delete_head

    def peek(self):
        if self.is_empty():
            return "Stack is Empty"
        return self.head.data

    # isEmpty 기능 구현
    def is_empty(self):
        return self.head is None

stack1 = Stack()
print(stack1.is_empty())
stack1.push(5)
print(stack1.peek())
print(stack1.is_empty())
stack1.push(4)
stack1.push(3)
print(stack1.pop())
print(stack1.pop())
print(stack1.pop())
print(stack1.is_empty())
