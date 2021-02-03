# [5, 3, 2, 1, 6, 8, 7, 4]
# [5] [3] -> [3, 5]
# [2] [1] -> [2, 1]
# [6] [8] -> [6, 8]
# [7] [4] -> [7, 4]
# ->
# [3, 5] [2, 1] -> [1,2,3,5]
# [6, 8] [7, 4] -> [4,6,7,8]
# ->
# [1,2,3,5] [4,6,7,8] -> [1,2,3,4,5,6,7,8]

# [1,2,3,4,5,6,7,8] 길이 : N
# 1단계 [1,2,3,5] [4,6,7,8] 길이 N/2 2개를 비교하면서 합침 -> N/2 * 2 = N 만큼의 시간 복잡도
# 2단계 [3, 5] [2, 1] -> [1,2,3,5] 길이 N/4 2개를 비교
# 3단계 [6, 8] [7, 4] -> [4,6,7,8] 길이 N/4 2개를 비교 -> N/4 * 2 * 2 = N 만큼의 시간 복잡도
# => 병합 정렬에서 병합하는 단계는 모든 단계에서 N 만큼의 시간 복잡도를 가지게 된다.
# ...
# k단계 [5] [3] ... 길이가 1일 때
# -> 즉 k단계를 거치면, 1이 된다.
# -> 수식 : N / 2^k = 1
# -> log2N
# -> 즉 k단계를 반복하는데 각각 단계는 O(N) 시간 복잡도를 가진다.
# -> 즉, log2N * O(N) -> O(NlogN)


array = [5, 3, 2, 1, 6, 8, 7, 4]

def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left_array = merge_sort(array[:mid]) # [5, 3, 2, 1]
    right_array = merge_sort(array[mid:]) # [6, 8, 7, 4]
    # print(array)
    # print('left_array', left_array)
    # print('right_array', right_array)
    return merge(left_array, right_array)

def merge(array1, array2):  # merge O(N)
    result = []
    array1_index = 0
    array2_index = 0
    while array1_index < len(array1) and array2_index < len(array2):
        if array1[array1_index] < array2[array2_index]:
            result.append(array1[array1_index])
            array1_index += 1
        else:
            result.append(array2[array2_index])
            array2_index += 1

    if array1_index == len(array1):
        while array2_index < len(array2):
            result.append(array2[array2_index])
            array2_index += 1

    if array2_index == len(array2):
        while array1_index < len(array1):
            result.append(array1[array1_index])
            array1_index += 1
    return result


print(merge_sort(array))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!