input = [4, 6, 2, 9, 1, 8]
# 4  6  2  9  1
# -  -  -  -  - 0~4
# 1  6  2  9  4
#    -  -  -  - 1~4
# 1  2  4  6  9
#       -  -  - 2~4
# 1  2  4  6  9
#          -  - 3~4

# 1. 시도할 index　읽히는지 for문 먼저 돌려보기
# 0~4, 1~4, 2~4, 3~4
# for i in range(5-1):
#     for j in range(5-i):
#         print(i+j)

# O(N^2)
def selection_sort(array):
    n = len(array)
    for i in range(n - 1):
        min_index = i
        for j in range(n - i):
            # i+j : 현재 시도해보고 있는 index
            if array[i + j] < array[min_index]:
                min_index = i + j
        array[i], array[min_index] = array[min_index], array[i]

    return

selection_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!