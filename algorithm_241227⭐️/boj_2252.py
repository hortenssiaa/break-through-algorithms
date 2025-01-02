# 위상 정렬 - queue 사용
from collections import deque

N, M = list(map(int, input().split()))

need_to_learn = [0] * N
adj = [[] for _ in range(N)]

for i in range(M):
    a, b = list(map(int, input().split()))
    adj[a - 1].append(b - 1)
    need_to_learn[b - 1] += 1

make_line = [] 
# 위상 정렬
queue = deque([])
for i in range(N):
    if need_to_learn[i] == 0:
        queue.append(i)

while len(queue) != 0:
    idx = queue.popleft()
    make_line.append(idx + 1)

    for i in adj[idx]:
        need_to_learn[i] -= 1
        # ⭐️⭐️⭐️⭐️⭐️⭐️
        if need_to_learn[i] == 0:
            queue.append(i)

for i in make_line:
    print(i, end=' ')


# deque 안쓰면 - 시간 초과
# while line_idx < N:
#     # 비교해야하는 횟수 0; 줄세우기
#     idx = need_to_learn.index(0)
#     need_to_learn[idx] = -1

#     make_line[line_idx] = idx + 1
#     line_idx += 1

#     for i in adj[idx]:
#         need_to_learn[i] -= 1

# for i in make_line:
#     print(i, end=' ') 
    