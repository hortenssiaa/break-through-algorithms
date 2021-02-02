input = [4, 6, 2, 9, 1, 7]

# 1. 반복문이 어떻게 돌아가는지 확인하기
# 4  6  2  9  1
#  <-  0,1
# 4  6  2  9  1
#  <- <- 0,1,2
# 2  4  6  9  1
#  <- <- <- 0,1,2,3
# 2  4  6  9  1
#  <- <- <- <- 0,1,2,3,4
# -> 1  2  4  6  9

# for i in range(1,5): # 1 ~ 4까지
#     for j in range(i):
#         print(i-j) # 1 / 2,1 / 3,2,1 / 4,3,2,1 ...


def insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        for j in range(i): # i-j : 1 / 2,1 / 3,2,1 / 4,3,2,1 ...# 1 / 2,1 / 3,2,1 / 4,3,2,1 ...
            if array[i-j-1] > array[i-j]: #　앞에 있는게, 뒤에 있는 것보다 클 때
                array[i-j], array[i-j-1] = array[i-j-1], array[i-j]
            else:
                # 그렇지 않은 경우는 바로 반복문 나가게 = 즉, 비교를 안해도 되는 순간
                # 즉, [1,2,3,4,5]를 insertion sort시; 1이 있을 때 2를 넣으려고 하면, 1보다 큰것을 아니 비교하지 않고 바로 넣는다.
                # => 거의 정렬이 된 배열의 경우, 삽입정렬을 사용하면 최선이 N이므로, 다른 두개 보다 조금 더 효율적이다!
                break
    return


insertion_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!