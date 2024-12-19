import sys
from queue import PriorityQueue

input = sys.stdin.readline

V, E = list(map(int, input().split()))
K = int(input()) - 1
adj = [[] for _ in range(V)]

# adj
for _ in range(E):
  u, v, w = list(map(int, input().split()))
  adj[u - 1].append((w, v - 1)) # w, index

dist = [1e9] * V # dist 확정
pq = PriorityQueue() # dist 개발중

dist[K] = 0
pq.put((0, K)) # (우선순위(w), 값(index))

# 다익스트라 priority queue
while pq.qsize() != 0:
    min_w, idx = pq.get() # (w, index) 형태 
    
    if min_w != dist[idx]:
       continue

    for w, v in adj[idx]: 
       if dist[v] > dist[idx] + w:
          dist[v] = dist[idx] + w
          pq.put((dist[v], v)) 
    
for i in range(V):
    if i == K:
      print(0)
    else:
        if dist[i] == 1e9:
          print("INF")
        else:
          print(dist[i]) 