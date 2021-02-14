# [None, 3, 4, 2, 9]
#     9(1)
#   4(2)   2(3)
# 3(4)
# 1. 마지막 원소부터 하나씩, 자신의 부모 (현재 인덱스 // 2) 와 비교
# 2. 자기 > (현재 인덱스 // 2) 이면, 값 바꿈

class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        self.items.append(value)
        cur_idx = len(self.items) - 1
        while cur_idx > 1:
            parent_idx = cur_idx // 2
            if self.items[cur_idx] > self.items[parent_idx]:
                self.items[cur_idx], self.items[parent_idx] = self.items[parent_idx], self.items[cur_idx]
                cur_idx = parent_idx
            else:
                break

        return self.items


max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(4)
max_heap.insert(2)
max_heap.insert(9)
print(max_heap.items)  # [None, 9, 4, 2, 3] 가 출력되어야 합니다!