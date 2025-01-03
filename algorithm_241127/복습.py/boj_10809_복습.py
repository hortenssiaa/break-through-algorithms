S = input()
check = [-1] * 26

for i in range(len(S)):
    ch = S[i]
    idx = ord(ch) - ord('a')
    if check[idx] == -1:
        check[idx] = i

for i in check:
    print(i, end=" ")