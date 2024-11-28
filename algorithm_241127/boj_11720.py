# my code
n = int(input())
number = input()

sum = 0
for i in range(n) :
  sum += int(number[i])

print(sum)


# tutor code
n = int(input())
number = input()

sum = 0
for i in range(n) :
  # (아스키 값) '9' - '0' = 9
  sum += (ord(number[i]) - ord('0'))

print(sum)