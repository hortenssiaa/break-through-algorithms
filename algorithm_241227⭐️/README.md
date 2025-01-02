## boj_2252⭐️ (줄세우기)
### 위상 정렬


### - 핵심 포인트
1. Queue (deque) 사용
2. 방향그래프의 노드를 1자로 나열하는데
   - 간선이 모두 왼쪽->오른쪽으로 
3. 비교 배열이 있음
   - (= 선수과목  = 화살표를 받는 횟수) 
4. 값이 여러개 있을 수 있음
   
<br>

### - ⭐️풀이 순서⭐️
1. 일단은 문제를 풀어보기
2. 비교해야하는 횟수가 0인 노드 -> 줄세우기
3. 해당 번호와 비교되는 adj 모두 -1 하기
4. -1 했을 때, 값이 0인 노드 -> queue.append()

<br>

```swift
whlie len(queue) != 0:
    idx = queue.popleft()
    make_line.append(idx + 1)

    for i in adj[idx]:
        need_to_learn[i] -= 1
        # ⭐️⭐️⭐️⭐️⭐️⭐️
        if need_to_learn[i] == 0:
            queue.append(i)
```
<br>


### - 위상 정렬
![Coding-105](https://github.com/user-attachments/assets/4fa0951f-e756-4e83-9654-e7b365eb7132) | ![Coding-106](https://github.com/user-attachments/assets/2eb5ac84-c4ca-4d6e-b785-b7ea1fba924c)
--- | --- |


<br>



### - 손글씨 정리

 ![Coding-107](https://github.com/user-attachments/assets/45e5cb8d-3e56-4196-ad8e-40674d3ed58d) | ![Coding-108](https://github.com/user-attachments/assets/21e93fbd-1aa3-47cd-8f74-248b4e4e10ee)
--- | --- |






<br>
<br>

---------------------------------------


