input = [4, 6, 2, 9, 1, 3]


def bubble_sort(array):
    first_index = 0
    last_index = len(array) - 1
    cur_index = 0

    # O(N^2)
    while cur_index < last_index: # n의 길이
        if array[cur_index] > array[cur_index + 1]:
            array[cur_index], array[cur_index + 1] = array[cur_index + 1], array[cur_index]
        cur_index += 1
        first_index += 1
        if cur_index >= last_index: # n의 길이
            cur_index = 0
            last_index -= 1

    return


bubble_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!