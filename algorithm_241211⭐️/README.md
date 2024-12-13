## boj_11724 (연결 요소의 개수)
### 그래프 탐색 (BFS)


### - 핵심 포인트
1. adj (인접 리스트) 사용
2. 시작점
3. visit 배열
4. 최단거리 배열
5. Queue

<br>

### - 손글씨 정리
![Coding-67](https://github.com/user-attachments/assets/f981a646-b72f-4807-bad7-aefa07654c90) | ![Coding-68](https://github.com/user-attachments/assets/c19f2c07-9e34-4d06-8a19-28465501d434) | ![Coding-69](https://github.com/user-attachments/assets/16a6a2bc-cfe9-467b-a160-36545c65bc03)
--- | --- | --- | 



<br>
<br>

---------------------------------------

<br>

## boj_1389 (케빈 베이컨의 6단계 법칙)
### 그래프 탐색 (BFS)


### - 핵심 포인트
1. adj (인접 리스트) 사용
2. 시작점
3. visit 배열
4. 최단거리 배열
5. Queue

### - ⭐️풀이 순서⭐️
1. adj (인접 리스트) 사용
2. 시작점을 기준 (0~N-1 모두 탐색)
3. 시작점 queue에 append
4. queue.pop
5. <⭐️1⭐️> pop한 adj index 확인
6. 확인한 adj index는, queue에 들여보내기 전, 먼저 확인!!
7. <⭐2⭐️> 확인 >> adj 순서대로, True; pass, False: queue추가 & 직전 pop한 index의 dist(최단거리) + 1

<br>



### - 손글씨 정리
![Coding-70](https://github.com/user-attachments/assets/c4c49877-9afe-4dae-b761-3e98f7f44047) | ![Coding-77](https://github.com/user-attachments/assets/70e01331-134e-4a41-a465-2a6e5700b023) 
--- | --- |
![Coding-71](https://github.com/user-attachments/assets/dba82adc-2a44-4af1-83c2-65e59a039a86) | ![Coding-72](https://github.com/user-attachments/assets/450c3e88-1e95-4721-8997-5b2d8adce5dc)  
