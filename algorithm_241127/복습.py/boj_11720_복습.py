N = int(input())
str_num = input()

sum = 0
# 안좋은 접근
# for i in range(N):
#     sum += int(str_num[i])

# tutor - 문자열이니, ord() 사용
# ASCII : '9' - '0' == 9
for i in range(N):
    sum += (ord(str_num[i]) - ord('0'))
print(sum)