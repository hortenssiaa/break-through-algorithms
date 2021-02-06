# 해쉬 : 데이터의 검색과 저장이 아주 빠르게 진행된다.

class Dict:
    def __init__(self):
        self.items = [None] * 8

    def put(self, key, value):
        self.items[hash(key) % len(self.items)] = value
        return

    def get(self, key):
        return self.items[hash(key) % 8]

my_dict = Dict()
my_dict.put("test", 3)
print(my_dict.get("test"))