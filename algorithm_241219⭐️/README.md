## boj_1753 (최단경로)
### 최단거리 알고리즘 (다익스트라 알고리즘)


### - 핵심 포인트
1. adj + 튜플(거리)
2. 우선순위 큐 (priority queue)
   
<br>

### - ⭐️풀이 순서⭐️
1. adj + 튜플(거리)
2. 우선순위 큐 사용하여, [dist 개발중 배열] 에서 최단거리 찾아서 
   -> [dist 확정 배열] 에 넣기
3.  [dist 확정 배열] 로 넣어진 노드의 인접노드 adj에서 update

<br>

```swift
for t, u in adj[idx]:
  if dist[idx] != t:
    continue // 이미 최단거리로 확정된 노드에 대해, adj로 인해 해당 노드를 읽을 시; 넘어간다 

  ...
```
<br>

### - 다익스트라 알고리즘

  
![Coding-86](https://github.com/user-attachments/assets/429bc512-568b-408d-a0d6-fe7264f92c12) | ![Coding-87](https://github.com/user-attachments/assets/a389a216-b71b-41b7-b19e-76c18c8a680f) | ![Coding-88](https://github.com/user-attachments/assets/31c4fd92-b70d-4b09-a5b1-62c831851062)
--- | --- | --- | 

<br>

### - 우선순위 큐 (Priority Queue)

![Coding-89](https://github.com/user-attachments/assets/6ec6504a-a887-4a81-bec1-475baacffd83) | ![Coding-90](https://github.com/user-attachments/assets/70c4114b-5d43-4123-9539-1b405d9e3cf9)
--- | --- | 

<br>

### - 손글씨 정리
![Coding-91](https://github.com/user-attachments/assets/95a881c6-8c2c-4980-b7e0-e91fbbb3f6df) | ![Coding-92](https://github.com/user-attachments/assets/303567a7-b88e-44c0-ae42-fa2145a277bc)
--- | --- | 



<br>
<br>

---------------------------------------

<br>

## boj_1238⭐️ (파티)
### 최단거리 알고리즘 (다익스트라 알고리즘)


### - 핵심 포인트
1. adj + 튜플(거리)
2. 역 adj
   - 방향이 있는 그래프
3. 우선순위 큐 (priority queue)

<br>

### - ⭐️풀이 순서⭐️
1. adj + 튜플(거리)
2. adj + 우선순위 큐 사용하여,
   - 시작점 X 에서 1~N 노드 까지의 최단거리 구하기
3. 역 adj + 우선순위 큐 사용하여,
   - 시작점 1~N 노드 전체에서 특정 노드 Y까지의 최단거리 구하기
   - 역 adj 를 사용하지 않으면, ‼️비효율 최강‼️
     - 1~N노드 전체의 최단거리를 구해서, 그중에 Y까지인 최단거리 뽑아 써야하니 비효율적이다.
    
<br>

```swift
for t, u in adj[idx]:
  if dist[idx] != t:
    continue // 이미 최단거리로 확정된 노드에 대해, adj로 인해 해당 노드를 읽을 시; 넘어간다 

  ...
```

<br>

### - 다익스트라 알고리즘

  
![Coding-86](https://github.com/user-attachments/assets/429bc512-568b-408d-a0d6-fe7264f92c12) | ![Coding-87](https://github.com/user-attachments/assets/a389a216-b71b-41b7-b19e-76c18c8a680f) | ![Coding-88](https://github.com/user-attachments/assets/31c4fd92-b70d-4b09-a5b1-62c831851062)
--- | --- | --- | 

<br>

### - 우선순위 큐 (Priority Queue)

![Coding-89](https://github.com/user-attachments/assets/6ec6504a-a887-4a81-bec1-475baacffd83) | ![Coding-94](https://github.com/user-attachments/assets/c7338e0c-87db-4c2d-bfd5-4ade7fe94abe) | ![Coding-95](https://github.com/user-attachments/assets/25a9c842-ba30-4273-bcf8-7ca0d7a942ac)
--- | --- | --- | 


<br>

### - 손글씨 정리
![Coding-93](https://github.com/user-attachments/assets/49162395-5868-4d97-87a2-edf867a1fd10) | ![Coding-94](https://github.com/user-attachments/assets/3575bb19-e31f-4dae-a58e-1269ac70a80b) | ![Coding-95](https://github.com/user-attachments/assets/56f8c3c7-ff3d-43b7-84db-34544df3bea5)
--- | --- | --- | 

![Coding-96](https://github.com/user-attachments/assets/78c9e41d-5cfb-4a82-91a5-b86d36212f1c) | ![Coding-97](https://github.com/user-attachments/assets/9dd082ea-9c47-4071-b9ca-4e08d0e1ff53)
--- | --- | 
