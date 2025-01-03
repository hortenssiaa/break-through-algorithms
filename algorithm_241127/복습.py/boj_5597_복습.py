student = [0] * 30
for _ in range(28):
    idx = int(input())
    student[idx - 1] = 1

for i in range(len(student)):
    if student[i] == 0:
        print(i + 1)
