# Binary Search Time Complexity : O
# -> bad time complexity compare to 06_is_existing_target_number_binary_tut.py
# size of finding_numbers : N

finding_target = 24
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
#                최솟값                 시도값                           최댓값
#                                        최소값        시도값            최댓값
#                                                        최소값 시도값   최댓값


def is_existing_target_number_binary(target, array):
    cur_min = 0
    cur_max = len(array) - 1  # 15
    find_count = 0

    while cur_min <= cur_max:
        mid_num = (cur_min + cur_max) // 2  # // : 몫
        for number in range(array[cur_min], array[mid_num]+1):  # down
            find_count += 1
            if target == number:
                print(find_count)
                return True
        else:
            cur_min = mid_num+1

    print(find_count)
    return False


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)