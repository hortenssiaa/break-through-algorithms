# [Stack] 4949 균형잡힌 세상
# ( with ) 아닌 경우
# [ with ] 아닌 경우
# ( or [ 만 있고 

while True:
  s = input()

  # 입력 값이 단지 '.' 일 경우, 종료
  if s == ".":
    break

  stack = []
  balanced = True
  
  for i in range(len(s)):
    if s[i] == "(" or s[i] == "[":
      stack.append(s[i])

    if s[i] == ")":
      # stack이 비어있으면 안됨
      if len(stack) == 0:
        balanced = False
        break
        
      last = stack.pop(-1)    
      if last != "(":
        balanced = False
        break

    if s[i] == "]":
      if len(stack) == 0:
        balanced = False
        break
        
      last = stack.pop(-1)    
      if last != "[":
        balanced = False
        break

  # stack 이 마지막에 비어있지 않아도 false (ex. [ '[' ])
  if len(stack) != 0:
    balanced = False

  if balanced:
    print("yes")
  else:
    print("no")