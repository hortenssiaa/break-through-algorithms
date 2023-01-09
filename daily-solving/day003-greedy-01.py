'''
Q. 거스름돈
거슬러 줘야할 동전의 최소 개수
'''

# my answer

change = 1260
x500 = change // 500 # 2
x100 = (change - 500 * x500) // 100 # 2
x50 = (change - (500 * x500 + 100 * x100))  // 50 # 1
x10 = (change - (500 * x500 + 100 * x100 + 50 * x50)) // 10

print(f"500: {x500}, 100: {x100}, 50: {x50}, 10: {x10}")

# answer example
n = 1260 # 거스름돈
count = 0 # 거스름동전 갯수

# 큰 단위의 화폐부터 차례대로 확인
# 거스름돈은 무관, 동전의 종류와 갯수에만 영향
coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin # 거스름동전 갯수
    n %= coin # 남은 거스름돈

print("동전의 최소 개수:", count)