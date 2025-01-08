N = int(input())
require = list(map(int, input().split()))
given_budget = int(input())

start = 0
end = max(require)
answer = -1

while start <= end:
    mid = (start + end) // 2

    sum = 0
    for i in range(N):
        sum += min(require[i], mid)

    if sum > given_budget: # end - 1
        end = (mid - 1)
    else: # sum <= given_budget
        if answer < mid:
            answer = mid
        start = (mid + 1)
    
print(answer)