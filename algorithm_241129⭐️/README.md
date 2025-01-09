## 이분탐색 
### 문제 boj_2512, 2343


### - ⭐핵심 포인트⭐
1. 탐색 값 지정
2. 탐색 범위 지정 (left, right, middle)
3. while left <= right: 으로 이분탐색
4. left, right 갱신
5. answer 변수 지정하면 깔끔

<br>

### - 핵심 코드
#### boj_2512 (예산)⭐️⭐️
```python
start = 0           # 2. 탐색 범위 지정
end = max(require)  # 2. 탐색 범위 지정
answer = -1         # 5. answer 변수 지정

while start <= end: # 3. 이분탐색
    mid = (start + end) // 2

    sum = 0
    for i in range(N):
        sum += min(require[i], mid)

     # 4. left, right 갱신
    if sum > given_budget: # end - 1
        end = (mid - 1)
    else: # sum <= given_budget
        if answer < mid:
            answer = mid
        start = (mid + 1)
    
print(answer)
```


<br>

#### boj_2343 (기타레슨)⭐️⭐️
```python
left = max(lecture) # 강의 중 최대 길이           # 2. 탐색 범위 지정
right = sum(lecture)                          # 2. 탐색 범위 지정

answer = -1                                   # 5. answer 변수 지정

# 이분탐색 ⭐️⭐️⭐️
while left <= right:
    mid = (left + right) // 2

    blueray = 1
    remain = mid
    for i in range(N):
        if lecture[i] > remain:
            blueray += 1
            remain = mid

        remain -= lecture[i]

    # 4. left, right 갱신
    if blueray <= M:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)      # 바로 answer이 답인 이유: 이분탐색의 결과이기 때문
```


<br>

### - 손글씨 정리
![Coding-129](https://github.com/user-attachments/assets/17af70ba-74ea-46cb-8fba-6226b4d01700) | ![Coding-130](https://github.com/user-attachments/assets/57a93c19-20c4-4f02-bf26-36f1e8f0b9e1) | ![Coding-131](https://github.com/user-attachments/assets/db9eacc3-05cb-48fc-bc50-f202b4896605)
--- | --- | --- | 

