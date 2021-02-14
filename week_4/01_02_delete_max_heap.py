class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        self.items.append(value)
        cur_index = len(self.items) - 1

        while cur_index > 1:  # cur_index 가 1이 되면 정상을 찍은거라 다른 것과 비교 안하셔도 됩니다!
            parent_index = cur_index // 2
            if self.items[parent_index] < self.items[cur_index]:
                self.items[parent_index], self.items[cur_index] = self.items[cur_index], self.items[parent_index]
                cur_index = parent_index
            else:
                break

    def delete(self):
        max_idx = 1
        cur_idx = max_idx
        max_value = self.items[max_idx]

        self.items[max_idx], self.items[-1] = self.items[-1], self.items[max_idx]
        del self.items[-1]

        # 가장 바닥에 도달하지 않을 때까지 : cur_idx의 왼쪽자식 <= 총개수 -1
        while (cur_idx * 2) <= len(self.items) - 1:
            # 자식 노드 둘 보다 부모 노드가 크거나
            # [max_idx]의 왼쪽 자식 : self.items[max_idx] * 2
            # [max_idx]의 오른쪽 자식 : self.items[max_idx] * 2 + 1
            if self.items[cur_idx * 2] > self.items[cur_idx]:  # 왼쪽자식이 더 크고
                if self.items[cur_idx * 2 + 1] > self.items[cur_idx]:
                    if self.items[cur_idx * 2 + 1] > self.items[cur_idx * 2]: # 왼 < 오른
                        self.items[cur_idx], self.items[cur_idx * 2 + 1] = self.items[cur_idx * 2 + 1], self.items[cur_idx]
                        cur_idx = cur_idx * 2 + 1
                        continue
                    else: # 왼 > 오른
                        self.items[cur_idx], self.items[cur_idx * 2] = self.items[cur_idx * 2], self.items[cur_idx]
                        cur_idx = cur_idx * 2
                        continue
                else:
                    self.items[cur_idx], self.items[cur_idx * 2] = self.items[cur_idx * 2], self.items[cur_idx]
                    cur_idx = cur_idx * 2
                    continue
            elif self.items[cur_idx * 2 + 1] > self.items[cur_idx]:  # 오른쪽자식이 더 크고
                self.items[cur_idx], self.items[cur_idx * 2 + 1] = self.items[cur_idx * 2 + 1], self.items[cur_idx]
                cur_idx = cur_idx * 2 + 1
                continue
            else:
                break


        return max_value  # 8 을 반환해야 합니다.


max_heap = MaxHeap()
max_heap.insert(8)
max_heap.insert(7)
max_heap.insert(6)
max_heap.insert(2)
max_heap.insert(5)
max_heap.insert(4)
print(max_heap.items)  # [None, 8, 7, 6, 2, 5, 4]
print(max_heap.delete())  # 8 을 반환해야 합니다!
print(max_heap.items)  # [None, 7, 5, 6, 2, 4]