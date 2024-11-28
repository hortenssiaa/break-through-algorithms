# my code
# S = "baekjoon"
# a, b, c, d, ... , z
# 처음 등장하는 위치** / 포함X: -1

#   0 1 2 3 4 5 6 7 == (#s1)에서 check배열의index안에 들어갈 값
#   b a e k j o o n 
# - a
# = 1 0 4 ... : == 전체알파벳배열check에서의 해당 알파벳의 index (#s1)
#   a b c d e f g ... z
#   1 0 -1 -1 2 ... 번째에 있다 : baekjoon 에 해당하는 자리 값
# check[체알파벳배열check에서의 해당 알파벳의 index (#s1)] = (#s1)에서 check배열의index안에 들어갈 값

s = input()
check = [-1] * 26

for i in range(len(s)) : # i 는, 해당 알파벳의 자리 
  index = ord(s[i]) - ord('a') # 해당 알파벳의 전체 알파벳안에서의 index

  if check[index] == -1:
    check[index] = i

for i in range(len(check)) :
  print(check[i], end= ' ')


# tutor code
# 내 코드와 동일함