# [Queue] 18258 큐2

# my code - 시간 초과
# 정수 저장 큐 구현
class Queue:
  def __init__(self):
    self.items = []
      
  def push(self, n):
    self.items.append(n)

  def pop(self):
    return -1 if len(self.items) == 0 else self.items.pop(0)

  def size(self):
    return len(self.items)

  def empty(self): # 비어있으면 1, 아니면 0
    return 1 if len(self.items) == 0 else 0

  def front(self):
    return -1 if len(self.items) == 0 else self.items[0]

  def back(self):
    return -1 if len(self.items) == 0 else self.items[-1]

queue = Queue()
N = int(input())

for i in range(N):
  command = input()

  if "push" in command:
    num = command.split()[-1] # split() default구분자: " "
    queue.push(num)
    continue
    
  if command in "pop":
    print(queue.pop())
    continue

  if command in "size":
    print(queue.size())
    continue

  if command in "empty":
    print(queue.empty())
    continue

  if command in "front":
    print(queue.front())
    continue

  if command in "back":
    print(queue.back())
    continue


# tutor code
# 
# # 1. sys.stdin.readline()
# input 함수를 사용하면 시간상 통과 불가
# 여러줄의 입력을 빠르게 받는 함수 >> sys.stdin.readline() 사용
# 
#  2. from collections import deque
#  deque 자료구조 선언

import sys
from collections import deque

N = int(input())
d = deque([])

for i in range(N):
  command = sys.stdin.readline()
  command = command.split() # split default 구분자: " " // push 1 > ['push', '1']

  if command[0] == "push":
    d.append(command[1])

  if command[0] == "pop":
    if len(d) == 0:
      print("-1")
    else:
      d.popleft()

  if command[0] == "size":
    print(len(d))

  if command[0] == "empty":
    if len(d) == 0:
      print("1")
    else:
      print("0")

  if command[0] == "front":
    if len(d) == 0:
      print("-1")
    else:
      print(d[0])

  if command[0] == "back":
    if len(d) == 0:
      print("-1")
    else:
      print(d[-1])

