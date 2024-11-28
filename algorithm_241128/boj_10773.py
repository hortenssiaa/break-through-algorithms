# [Stack] 10773 제로

# my code
# 재민 <- 재현
# 잘못된수 : 0 -> 가장 최근에 쓴 수 지운다

# k = int(input())
# n = []
# for i in range(k) :
#     n.append(int(input()))

# result = []
# j = 0
# for i in range(len(n)) :
#     if n[i] == 0:
#         if i-1 >= 0:
#             j -= 1
#             del result[j]
#             continue

#     result.append(n[i])
#     j += 1

# print(sum(result))


#  my code 
k = int(input())
stack = []
for i in range(k) :
    num = int(input()) # 1 3 5 4 0
    
    if num == 0:
        stack.pop()
        continue

    stack.append(num) # 1 3 5 4 

print(sum(stack))


# tutor code
k = int(input())
stack = []

for i in range(k):
    n = int(input())
    if n == 0:
        stack.pop(-1)
    else:
        stack.append(n)

print(sum(stack))