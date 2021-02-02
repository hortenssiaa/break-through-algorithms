input = [4, 6, 2, 9, 1, 8]
# -> -> -> -> ->
# 4  6  2  9  1
#    -> -> -> ->
# 1  6  2  9  4
#      -> -> ->
# 1  2  4  6  9

def selection_sort(array):
    n = len(array)
    min_index = 0

    for i in range(n): # 0 1 2 3 4
        min = array[i]
        for j in range(i, n): # 0~4, 1~4, 2~4, 3~4, 4
            if array[j] < min:
                min = array[j]
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]

    return

selection_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!