# 💔 Breaking Through Algorithms 
### Contents

1. [Python grammer for coding-test](https://github.com/hortenssiaa/break-through-algorithms/blob/master/README.md#1-python-grammer-for-coding-test-code)
2. [Python library for coding-test](https://github.com/hortenssiaa/break-through-algorithms/blob/master/README.md#2-python-library-for-coding-test-code)

----
<br>

### 1. Python grammer for coding-test ([code](https://github.com/hortenssiaa/break-through-algorithms/blob/master/daily-solving/day001-python-grammer.py)) 
1.1 [자료형](https://github.com/hortenssiaa/break-through-algorithms/blob/master/README.md#11-자료형)
<br>
1.2 [List](https://github.com/hortenssiaa/break-through-algorithms/blob/master/README.md#12-list)
<br>
1.3 [문자열](https://github.com/hortenssiaa/break-through-algorithms/blob/master/README.md#13-문자열)
<br>
1.4 [튜플](https://github.com/hortenssiaa/break-through-algorithms/blob/master/README.md#14-튜플)
<br>
1.5 [Dictionary 사전](https://github.com/hortenssiaa/break-through-algorithms/blob/master/README.md#15-dictionary-사전)
<br>
1.6 [Set 집합](https://github.com/hortenssiaa/break-through-algorithms/blob/master/README.md#16-set-집합)
<br>
1.7 [조건문](https://github.com/hortenssiaa/break-through-algorithms/blob/master/README.md#17-조건문)
<br>
1.8 [반복문](https://github.com/hortenssiaa/break-through-algorithms/blob/master/README.md#18-반복문)
<br>
1.9 [함수](https://github.com/hortenssiaa/break-through-algorithms/blob/master/README.md#19-함수)

<br>
<br>

#### 1.1 자료형
- e
- 소수점 값 비교

<br>


#### 1.2 List
##### 1.2.1 list comprehension
```python
'''0부터 19까지의 수 중에서 홀수만 포함하는 리스트'''
array = [i for i in range(20) if i % 2 == 1]
print(array) # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

'''1부터 9까지의 수의 제곱 값을 포함하는 리스트'''
array = [i*i for i in range(1, 10)]
print(array) # [1, 4, 9, 16, 25, 36, 49, 64, 81]

'''n X m 크기의 2차원 리스트 초기화'''
'''
Usage of underbar _ ?
> 값 상관없이, 반복 횟수만 중요할 때 사용! 
'''
n = 3
m = 4
array = [[0]*m for _ in range(n)]
print(array) # [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
```

##### 1.2.2 list function
```python
# 변수명.count(특정값) : O(N)
a = [1, 4, 3, 1]
print(a.count(1)) # 2

# 변수명.remove(특정값) : O(N)
a.remove(3)
print(a) # [1, 4, 1]



'''함수 쓰지않고, remove_set 리스트에 포함안된 값만 저장하기
>> 시간복잡도 고려한 풀이 '''
a = [1, 2, 3, 4, 5, 5, 5]
remove_set = [3, 5]

result = [i for i in a if i not in remove_set]
print(result) # [1, 2, 4]

```

<br>


#### 1.3 문자열
```python
a = "ABCDEF"
print(a[2:4]) # CD
```

<br>


#### 1.4 튜플
- 튜플은 한번 선언된 값을 변경할 수 없다.
- ( ) 이용
- 튜플로 변경하면 안되는 값 변경되고 있지 않은지 체크 가능
- 그래프 알고리즘 구현시 많이 사용
  > 예) 다익스트라 최단경로 알고리즘에서, 내부에서 우선순위 큐 이용하는데, 이때 큐는 튜플로 작성됨
    > > (비용, 노드번호) 형태로 묶어서 관리

```python
a = (1, 2, 3, 4)
print(a) # (1, 2, 3, 4)

# a[2] = 7 # error
```

<br>


#### 1.5 Dictionary 사전
- 데이터의 검색 / 수정 : O(N)

```python
data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

if '사과' in data:
    print("사과 yes!")
```

<br>


#### 1.6 Set 집합
- 특정원소 존재유무 : O(N)

##### 1.6.1 집합 초기화 방법
```python
data = set([1, 1, 2, 3, 4, 4, 5])
print(data)

data = {1, 1, 2, 3, 4, 4, 5}
print(data)
```

##### 1.6.2 집합 연산
```python
a = set([1, 2, 3, 4, 5])
b = set([3, 4, 5, 6, 7])

# 합집합
print(a | b) # {1, 2, 3, 4, 5, 6, 7}

# 교집합
print(a & b) # {3, 4, 5}

# 차집합
print((a - b)) # {1, 2}
```


<br>

<table style="text-align: center;">
  <tr>
    <td>List</td>
    <td>튜플</td>
    <td>집합</td>
    <td>사전</td>
  </tr>  
  <tr>
    <td>[ ]</td>
    <td>( )</td>
    <td>{ }</td>
    <td>[k,v]</td>
  </tr>
  <tr>
    <td colspan="4">in, not in</td>
  </tr>
</table>

<br>

#### 1.7 조건문
##### 1.7.1 pass
```python
'''조건문 값이 참이라도, 아무것도 처리하고 싶지 않을때 pass 이용'''
score = 82
if score >= 80:
    pass # 나중에 작성할 코드
else:
    print("성적이 낮아요")
```

##### 1.7.2 conditional expression 조건부 표현식
```python
'''변수 = true일때값(1) if조건문(2) else(3) false일때값(4)'''
score = 85
result = "Success" if score >= 80 else "Fail"

print(result)
```

##### 1.7.3 리스트에 있는 원소의 값을 변경해서, 또 다른 리스트를 만들고자 할때
```python
a = [1, 2, 3, 4, 5]
remove = [3, 5]

result = [i for i in a if i not in remove]
print(result) # [1, 2, 4]
```

##### 1.7.4 수학 부등식 그대로 사용가능!
```python
x = 15
if x > 0 and x < 20:
    print(f"0 < {x} < 20")

if 0 < x < 20:
    print(f"0 < {x} < 20")
```

<br>

#### 1.8 반복문
##### 1.8.1 중첩 반복문
- 플로이드 워셜 알고리즘
- 다이나믹 프로그래밍 등에서 많이 사용된다.

```python
scores = [90, 85, 77, 65, 97]
cheating_list = [2, 4]

for i in range(5):
    if i + 1 in cheating_list:
        continue
    if scores[i] >= 80:
        print(i + 1, "번 학생은 합격입니다.")
```



<br>

#### 1.9 함수
- 문제 푸는 코드를 함수화하면, 매우 효과적으로 풀 수 있다.

##### 1.9.1 global
- 함수 안에서, 함수 밖의 변수 데이터를 변경해야하는 경우

```python
a = 0

def func():
    global a
    a += 1

for i in range(10):
    func()

print(a) # 10
```

##### 1.9.2 람다 표현식
- python의 정렬 라이브러리를 사용할때, 정렬 기준 (key)를 설정할 때에도 자주 사용된다.
```python
def add(a, b):
    return a+b

# 일반적인 add() 메서드 사용
print(add(3, 7))

# 람다 표현식으로 구현한 add() 메서드
print( (lambda a, b: a+b)(3, 7) )
```




<br>

#### 1.10 입출력
##### 1.10.1 입력을 위한 전혁적인 소스코드
 ```list(map(int, input().split()))```
 
```python
# ex 1)
# 데이터의 개수 입력
n = int(input())
# 각 데이터를 공백으로 구분하여 입력
data = list(map(int, input().split()))

data.sort(reverse=True)
print(data)
'''
input
5
65 90 75 34 99
result
[99, 90, 75, 65, 34]
'''


# ex 2)
# n, m, k를 공ㅇ백으로 구분하여 입력
n, m, k = map(int, input().split())
print(n, m, k)
```

<br>

##### 1.10.2 더 빠른 코드 - sys.stdin.readline()
- sys 라이브러리를 사용할때는, 한 줄 입력을 받고 나서 rstrip() 을 꼭 호출해야 한다.
- sys.stdin.readline() 까지만 작성하면, 입력 후 엔터가 줄바꿈 기호로 입력된다. 
   > 이때 이 공백 문자를 제거하려면, rstrip() 함수를 사용해야한다. 
 
```python
import sys

# 문자열 입력받기
data = sys.stdin.readline().rstrip()
print(data)
'''


# ex 2)
# n, m, k를 공ㅇ백으로 구분하여 입력
n, m, k = map(int, input().split())
print(n, m, k)
```


<br>

##### 1.10.3 변수를 문자열로 출력

```python
answer = 7

print("정답은 " + answer + " 입니다.") # error
print("정답은 " + str(answer) + "입니다.") # 정답은 7입니다.
print("정답은", answer, "입니다.") # 정답은 7 입니다. (띄어쓰기 포함! )
print(f"정답은 {answer}입니다.") # 정답은 7입니다.
```


<br>


----
<br>




### 2. Python library for coding-test ([code](https://github.com/hortenssiaa/break-through-algorithms/blob/master/daily-solving/day002-python-library.py))
