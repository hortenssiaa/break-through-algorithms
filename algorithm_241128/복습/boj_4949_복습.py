result = []
while True:
    s = input()
    if s == ".":
        break

    balanced = True
    stack = []
    for i in range(len(s)):
        if s[i] == "[" or s[i] == "(":
            stack.append(s[i])
        
        if s[i] == "]":
            if len(stack) == 0:
                balanced = False
                break

            if stack.pop() != "[":
                balanced = False
                break
                

        if s[i] == ")":
            if len(stack) == 0:
                balanced = False
                break

            if stack.pop() != "(":
                balanced = False
                break

    if len(stack) != 0:
        balanced = False

    if balanced:
        result.append("yes")
    else:
        result.append("no")

for i in result:
    print(i)