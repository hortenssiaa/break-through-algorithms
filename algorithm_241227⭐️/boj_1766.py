# 위상정렬
from queue import PriorityQueue

N, M = list(map(int, input().split()))
adj = [[] for _ in range(N)]
compare = [0] * N

for i in range(M):
    A, B = list(map(int, input().split()))
    adj[A - 1].append(B - 1)
    compare[B - 1] += 1

# 위상정렬
order_of_solution = []
pq = PriorityQueue()

for i in range(N):
    if compare[i] == 0:
        pq.put(i)

while pq.qsize() != 0:
    idx = pq.get()
    order_of_solution.append(idx + 1)

    for i in adj[idx]: # adj[0] == 2, 4
        compare[i] -= 1
        if compare[i] == 0:
            pq.put(i)

for i in range(N):
    print(order_of_solution[i], end=" ")