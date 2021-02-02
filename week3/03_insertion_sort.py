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
#     for j in range(i-1, -1, -1): # i:2 (1) , i:3 (2,1)
#         print(i,j)


def insertion_sort(array):
    n = len(array)
    for i in range(1, n):  # 1 ~ 4까지
        max_index = i
        for j in range(i-1, -1, -1): # (i-1) ~ 0
            if array[j] > array[max_index]:
                array[j], array[max_index] = array[max_index], array[j]
                max_index = j

    return


insertion_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!