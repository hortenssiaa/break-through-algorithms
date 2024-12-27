## boj_1463 (1로 만들기)
### Dynamic Programming (다이나믹 프로그래밍)


### - 핵심 포인트
1. 점화식 만들기
   - 일단은 문제를 풀어보기
   - 점화식으로 표현할, 패턴 찾기
2. min() 
   
<br>

### - ⭐️풀이 순서⭐️
1. 일단은 문제를 풀어보기
2. 점화식으로 표현할, 패턴 찾기
3. 3의 배수일때, 2의 배수일때, 그 외의 숫자 별로 코딩

<br>

```swift
for i in range(2, N+1): # N까지
    a[i] = 1 + a[i - 1]
    
    if i % 3 == 0: # 3의 배수
        a[i] = min(a[i], 1 + a[i // 3])

    if i % 2 == 0: # 2의 배수
        a[i] = min(a[i], 1 + a[i // 2])
```
<br>


### - Dynamic Programming
<img src="https://github.com/user-attachments/assets/88715bcc-7799-49b5-ae58-d5243f62c8a2" width="400" >



<br>



### - 손글씨 정리

![Coding-100](https://github.com/user-attachments/assets/ca4cc236-220c-4a02-b91b-f7dbc05dc2a2) | ![Coding-101](https://github.com/user-attachments/assets/03e79415-5b87-4e95-b056-d92e190eef5e) | ![Coding-102](https://github.com/user-attachments/assets/88b454be-3cf7-4809-b149-4bb2084a6d3c)
--- | --- | --- | 




<br>
<br>

---------------------------------------


## boj_2579⭐️ (계단 오르기)
### Dynamic Programming (다이나믹 프로그래밍)


### - 핵심 포인트
1. 점화식 만들기
   - 점화식을 만드는데, 첫 아이디어가 중요하다..
   
<br>

### - ⭐️풀이 순서⭐️
1. 일단은 문제를 풀어보기
2. 점화식으로 표현할, 패턴 찾기
   - 점화식 표현만 하면 됨.. 그게 전부..
     > aN : N 번째 -> 최대 점수  (⭐️바로 전 계단 밟지 X)
      
     > bN : N 번째 -> 최대 점수  (⭐️바로 전 계단 밟지 O)

<br>

```swift
A[0] = S[0]
B[0] = S[0]

for i in range(1, N):
    if i >= 2:
        A[i] = S[i] + max(A[i - 2], B[i - 2])
    else:
        A[i] = S[i]
    
    if i >= 3:
        B[i] = S[i] + S[i - 1] + max(A[i - 3], B[i - 3])
    else:
        A[i] = S[i] + S[i - 1]
```
<br>


### - Dynamic Programming
<img src="https://github.com/user-attachments/assets/88715bcc-7799-49b5-ae58-d5243f62c8a2" width="400" >



<br>

### - 손글씨 정리

![Coding-103 2](https://github.com/user-attachments/assets/2bc9eada-1bde-4dc3-8b72-59330658b6d6) | ![Coding-104 2](https://github.com/user-attachments/assets/d78cdb9c-a438-43f6-a010-bdc8e43594d7)
--- | --- |



