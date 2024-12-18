import sys
input = sys.stdin.readline

N = int(input())
adj = [[] for _ in range(N)]

for i in range(N-1):
    a, b = list(map(int, input().split()))
    adj[a - 1].append(b - 1)
    adj[b - 1].append(a - 1)

visit = [False] * N
parent = [-1] * N

# bfs
def bfs(v):
    visit[v] = True

    for i in adj[v]:
        if not visit[i]:
            parent[i] = v
            bfs(i)
        # else:
        #     parent[v] = i+1

bfs(0)

for i in range(1, N):
    print(parent[i]+1)