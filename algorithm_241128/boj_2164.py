# [Queue] 2164 카드2
# My code - 시간초과
from collections import deque

N = int(input())
d = deque([])

for i in range(N):
  d.append(i+1)

while True:
  if len(d) >= 2:
    d.popleft() # 맨 위 버리고
  
    if len(d) == 1:
      print(d[0])
      break
    else:
      top = d.popleft() # 맨 위를 빼서 맨 아래로
      d.append(top)


# tutor code
from collections import deque

N = int(input())
d = deque(list(range(1, N+1))) # 초기화 

drop = True

while len(d) > 1: # deque길이가 1일때 까지 (2 까지는 괜찮으니깐)
    if drop:
        d.popleft()
        drop = False
    else:
        top = d.popleft()
        d.append(top)
        drop = True

print(d[0])