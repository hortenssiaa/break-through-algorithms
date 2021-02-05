# 실전에서는 [] (list)를 스택에 사용한다. - [], .pop()
# O(N^2)

top_heights = [6, 9, 5, 7, 4]
# [0, 0, 0, 0, 0] -> 답 : [0, 0, 2, 2, 4]

#  <- <- <- <-
#          7  4
# [0, 0, 0, 0, 4] - index

#  <- <- <-
# 6  9  5  7
# [0, 0, 0, 2, 4]

#  <- <-
# 6  9  5
# [0, 0, 2, 2, 4]

#  <-
# 6  9
# [0, 0, 2, 2, 4]

# 6 -> 마지막 하나 남은 6은 더이상 비교할 필요없음!

def get_receiver_top_orders(heights): # -> O(N^2)
    answer = [0] * len(heights) # [0, 0, 0, 0, 0]

    # [6, 9, 5, 7, 4]
    while heights: # heights가 빈 상태가 아닐때 까지, O(N)
        height = heights.pop()
        # [6, 9, 5, 7]
        for idx in range(len(heights)-1, -1, -1): # 3,2,1,0  2,1,0,  O(N)
            if heights[idx] > height:
                answer[len(heights)] = idx + 1 # why len(heights)?　현재 heights의 len(heights)번째가 비교하는 대상인 원 heights의본 index이기 때문에!
                break
    return answer

print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!