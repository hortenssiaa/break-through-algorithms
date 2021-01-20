input = [3, 5, 6, 1, 2, 4]

# N*1 = N -> O(N)
# Ω(1)
# -> 운이 좋으면, 1번만에 답을 찾을 수 있음
# 알고리즘 : 입력값에 따라서 성능이 변화한다.
def is_number_exist(number, array):
    for num in array: # array 길이 : N
        if number == num: # 비교 연산 : 1번 실
            return True
    return False

result = is_number_exist(7, input)
print(result)