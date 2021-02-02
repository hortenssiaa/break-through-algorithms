input = [4, 6, 2, 9, 1]
#  -> -> -> ->  4번 비교
# 4  6  2  9  1
#  ->  -> ->   3번 비교
# 4  2  6  1  9
#  ->  ->   2번 비교
# 2  4  1  6  9
#  ->   1번 비교
# 2  1  4  6  9

def bubble_sort(array):
    n = len(array)
    # O(N^2)
    for i in range(n - 1): # 0~4, 0~3, 0~2, 0~1, 0 이렇게 뒤에서 하나씩 줄어드는 만큼 하는 거니깐!, n의 길이
        for j in range(n - i - 1): # 4번, 3번, 2번, 1번 비교     , n의 길이
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return


bubble_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!