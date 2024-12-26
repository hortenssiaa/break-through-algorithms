N = int(input())

S = [0] * (N + 1)
for i in range(1, N + 1): 
    S[i] = int(input())

A = [0] * (N + 1)
B = [0] * (N + 1)

for i in range(1, N + 1):
    if i >= 2:
        A[i] = S[i] + max(A[i - 2], B[i - 2])
    else:
        A[i] = S[i]
    
    if i >= 3:
        B[i] = S[i] + S[i - 1] + max(A[i - 3], B[i - 3])
    else:
        A[i] = S[i] + S[i - 1]

print(max(A[N], B[N]))