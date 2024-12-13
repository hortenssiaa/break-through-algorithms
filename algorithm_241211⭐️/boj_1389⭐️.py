import sys
from collections import deque

input = sys.stdin.readline

N, M = list(map(int, input().split()))

# 인접리스트
adj = [[] for _ in range(N)]

for _ in range(M):
  u, v = list(map(int, input().split()))
  adj[u - 1].append(v - 1)
  adj[v - 1].append(u - 1)

min_kevin_bacon = 1e9
min_person = -1

for startPoint in range(N):
  # startPoint를 시작점으로 하는 BFS 
  # 각 노드까지의 최단거리를 구해서 다 합치기
  visit = [False] * N
  dist = [-1] * N

  visit[startPoint] = True
  dist[startPoint] = 0
  queue = deque([startPoint])

  while len(queue) != 0:
    q = queue.popleft()

    for v in adj[q]:
      if not visit[v]:
        queue.append(v)
        visit[v] = True
        dist[v] = dist[q] + 1
  
  if min_kevin_bacon > sum(dist):
    min_kevin_bacon = sum(dist)
    min_person = startPoint + 1

print(min_person)