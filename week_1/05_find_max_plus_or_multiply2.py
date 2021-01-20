input = [0, 3, 5, 6, 1, 2, 4]

# tutor's solution
# O(N) : 반복문 1번, 계수는 다 버리고
def find_max_plus_or_multiply(array):
    cal_result = 0

    for num in array:
        if num <= 1 or cal_result <= 1:
            cal_result += num
        else:
            cal_result *= num

    return cal_result


result = find_max_plus_or_multiply(input)
print(result)