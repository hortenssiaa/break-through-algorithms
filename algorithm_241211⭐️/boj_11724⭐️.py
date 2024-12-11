# import sys
# from collections import deque

# input = sys.stdin.readline

# N, M = list(map(int, input().split()))

# adj = [[] for _ in range(N)]

# for _ in range(M):
#   u, v = list(map(int, input().split()))

#   # adj 구하기
#   adj[u - 1].append(v - 1)
#   adj[v - 1].append(u - 1)

# visit = [False] * N
# count = 0

# for i in range(N): # i: 0 F->T, 1 T, 2 T, 3 F
#   if visit[i]:
#     continue
  
#   # BFS 시작
#   count += 1 # i:0 >count:1 // i:3 >count:2

#   queue = deque([i]) # 0 // 3
#   visit[i] = True # 0 F->T // 3 F->T
  
#   while len(queue) != 0:
#     q = queue.popleft() # 0 T (x) // 1 T (o) >len(queue):1 // 2 T (O) >len(queue):0

#     for v in adj[q]: # 1 F, 2 F // 0 T, 2 T // 0 T, 1 T
#       if not visit[v]: 
#         visit[v] = True # 1 T, 2 T // 
#         queue.append(v) # 1 T (o), 2 T (o) >len(queue):2

# print(count)

from collections import deque

queue = deque
print(queue)

queue = deque([1])
print(queue)

queue.append(2)
print(queue)