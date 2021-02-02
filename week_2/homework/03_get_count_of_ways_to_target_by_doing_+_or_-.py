# 문제가 축소되는 과정에서는 재귀함수로 해결할 수 있다는 생각!
# 내가 지금 헷갈리는 것이 있다면, 모든 경우의 수를 다 써보고 -> try 해보자!!
# call by reference , global 변수 googling!

numbers = [1, 1, 1, 1, 1]
target_number = 3

result_count = 0

def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, current_index, current_sum):
    if current_index == len(array):
        if current_sum == target:
            global result_count
            result_count += 1
        return

    get_count_of_ways_to_target_by_doing_plus_or_minus(
        array, target, current_index + 1, current_sum + array[current_index]
    ) # get_count_of_ways_to_target_by_doing_plus_or_minus(array, 1, 0 + 2, all_ways)

    get_count_of_ways_to_target_by_doing_plus_or_minus(
        array, target, current_index + 1, current_sum - array[current_index]
    ) # get_count_of_ways_to_target_by_doing_plus_or_minus(array, 1, 0 - 2, all_ways)


get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number, 0, 0)  # 5를 반환해야 합니다!
print(result_count)