## boj_2606 (바이러스)
### 그래프 탐색 (DFS)


### - 핵심 포인트
1. adj (인접 리스트) 사용
2. dfs 재귀함수 이용
3. visit 배열
4. (Stack)

<br>

### - ⭐️풀이 순서⭐️
1. adj (인접 리스트) 사용
2. dfs 재귀함수 이용
```swift
# bfs
def bfs(v):
    visit[v] = True

    for i in adj[v]:
        if not visit[i]:
            parent[i] = v
            bfs(i)
        # else:
        #     parent[v] = i+1
```

<br>

### - 손글씨 정리
![Coding-78 2](https://github.com/user-attachments/assets/0b938cee-004a-43b9-9fdb-8241e0ca8df1) | ![Coding-79 2](https://github.com/user-attachments/assets/38f72cd8-f226-43c6-b05f-18c3157b90b0) | ![Coding-80](https://github.com/user-attachments/assets/8add1278-e08d-402f-a2c0-f91893f08e22)
--- | --- | --- | 



<br>
<br>

---------------------------------------

<br>

## boj_11725 (트리의 부모 찾기)
### 그래프 탐색 (DFS)


### - 핵심 포인트
1. adj (인접 리스트) 사용
2. dfs 재귀함수 이용
3. visit 배열
4. parent 배열 
5. (Stack)

<br>

### - ⭐️풀이 순서⭐️
1. adj (인접 리스트) 사용
2. dfs 재귀함수 이용
```swift
# bfs
def bfs(v):
    visit[v] = True

    for i in adj[v]:
        if not visit[i]:
            parent[i] = v
            bfs(i)
        # else:
        #     parent[v] = i+1
```

<br>


### - 손글씨 정리
![Coding-78 2](https://github.com/user-attachments/assets/0b938cee-004a-43b9-9fdb-8241e0ca8df1) | ![Coding-79 2](https://github.com/user-attachments/assets/38f72cd8-f226-43c6-b05f-18c3157b90b0)  | ![Coding-85](https://github.com/user-attachments/assets/99178ec3-8704-47cc-87b2-ba212818b953)
--- | --- | --- |
