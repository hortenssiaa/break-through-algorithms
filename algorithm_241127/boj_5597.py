# my code
check = [0] * 30
for i in range(28) :
  inputResult = int(input())
  check[inputResult-1] += 1

for i in range(30):
  if check[i] == 0 :
    print(i+1, end="\n")


# tutor code
check = [0] * 31

for i in range(28) :
  n = int(input())
  check[n] = 1 # 0 -> 1

answer = []
for i in range(1, 31) :
  if check[i] == 0 :
    answer.append(i)

print(answer[0])
print(answer[1])