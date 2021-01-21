# 배열 속 무작위 수 찾기

finding_target = 2
finding_numbers = [0, 3, 5, 6, 1, 2, 4]

def is_exist_target_number_binary(target, numbers):
    cur_min_index = 0
    cur_max_index = len(finding_numbers) - 1

    while cur_min_index <= cur_max_index:
        cur_guess_index = (cur_max_index + cur_min_index) // 2
        for number in range(cur_min_index, cur_guess_index + 1):  # down
            if numbers[number] == target:
                return True
        else:
            cur_min_index = cur_guess_index + 1

    return False


result = is_exist_target_number_binary(finding_target, finding_numbers)
print(result)