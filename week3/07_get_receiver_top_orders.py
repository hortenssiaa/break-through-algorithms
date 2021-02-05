# 실전에서는 [] (list)를 스택에 사용한다. - [], .pop()

# top_heights = [6, 9, 5, 7, 4]
#         답 : [0, 0, 1(9), 1(9), 3(7)]
top_heights = [6, 9, 5, 7, 4, 10]
#         답 : [0, 0, 1(9), 1(9), 3(7), 0]

# print(top_heights)
# for i in reversed(top_heights):
#     print(i)
# print(top_heights)

# for index in range(len(top_heights)-1,-1,-1):
#     print(index)

def get_receiver_top_orders(heights):
    heights_store = []
    n = len(heights)

    for i in range(n): # 5번 반복
        count = 0
        top_receiver = heights.pop() # 4 7
        for height in range(len(top_heights)-1,-1,-1): # height = 4 7 5 9 6
            if heights[height] == heights[0]:
                heights_store.append(0)
                break
            if heights[height] > top_receiver:
                heights_store.append(height+1)
                break
            else:
                count += 1
        if count == len(heights):
            heights_store.append(0)

    return heights_store[::-1]


print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!