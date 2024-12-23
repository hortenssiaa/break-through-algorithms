import sys
from queue import PriorityQueue

input = sys.stdin.readline

N, M, X = list(map(int, input().split()))
X -= 1
adj = [[] for _ in range(N)]
adj_reverse = [[] for _ in range(N)]

# adj
for _ in range(M):
    a, b, w = list(map(int, input().split()))
    adj[a - 1].append((w, b - 1))
    adj_reverse[b - 1].append((w, a - 1))

dist = [1e9] * N
pq = PriorityQueue()

dist[X] = 0 # dist 확정  
pq.put((0, X)) # dist 개발중

while pq.qsize() != 0:
    t, idx = pq.get()
    
    if t != dist[idx]:
        continue

    for x_t, x_idx in adj[idx]:
        if dist[x_idx] > dist[idx] + x_t:
            dist[x_idx] = dist[idx] + x_t
            pq.put((dist[x_idx], x_idx))

# reverse adj
dist_reverse = [1e9] * N

dist_reverse[X] = 0 # dist 확정  
pq.put((0, X))

while pq.qsize() != 0:
    t, idx = pq.get()

    if t != dist_reverse[idx]:
        continue
    
    for x_t, x_idx in adj_reverse[idx]:
        if dist_reverse[x_idx] > dist_reverse[idx] + x_t:
            dist_reverse[x_idx] = dist_reverse[idx] + x_t
            pq.put((dist_reverse[x_idx], x_idx))

max = -1
for i in range(N):
    sum = dist[i] + dist_reverse[i]
    if sum > max:
        max = sum

print(max)