# dfs
# *** 재귀함수 dfs 이용
import sys

input = sys.stdin.readline

N = int(input())
M = int(input())

# adj
adj = [[] for _ in range(N)]
for _ in range(M):
  u, v = list(map(int, input().split()))
  adj[u - 1].append(v - 1)
  adj[v - 1].append(u - 1)

visit = [False] * N
# dfs
def dfs(u):
  visit[u] = True
  
  for i in adj[u]:
    if not visit[i]:
      dfs(i)

dfs(0)

count = 0
for i in range(1, N):
  if visit[i]:
    count += 1

print(count)