# Binary Search Time Complexity : O(logN)
# -> N / 2 / 2 / 2 .... -> repeating k times = N/2^k
# -> N/2^k = 1 이 마지막
# -> = logN
# size of finding_numbers : N

finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
#                최솟값                 시도값                           최댓값
#                                        최소값        시도값            최댓값
#                                                        최소값 시도값   최댓값


def is_existing_target_number_binary(target, array):
    cur_min_index = 0 # index
    cur_max_index = len(array) - 1  # index 15
    cur_guess_index = (cur_max_index + cur_min_index) // 2
    find_count = 0  # time complexity

    while cur_min_index <= cur_max_index:
        find_count += 1

        if array[cur_guess_index] == target:
            print(find_count)
            return True
        elif array[cur_guess_index] < target:  # up
            cur_min_index = cur_guess_index + 1
        else:  # down
            cur_max_index = cur_guess_index -1
        cur_guess_index = (cur_max_index + cur_min_index) // 2

    print(find_count)
    return False


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)