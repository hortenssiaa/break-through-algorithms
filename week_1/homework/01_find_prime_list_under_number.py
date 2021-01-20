input = 33

# 입력값 이하의 소수 구하기
def find_prime_list_under_number(number):
    prime_list = []

    for num in range(1, number+1):
        if num % 2 == 0 or num % 3 == 0:
            if num == 2 or num == 3:
                prime_list.append(num)
            continue
        else:
            prime_list.append(num)

    return prime_list


result = find_prime_list_under_number(input)
print(result)