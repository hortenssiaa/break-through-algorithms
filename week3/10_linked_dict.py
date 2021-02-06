# 충돌 시 : Linked List로, 충돌시 추가해 주자!
# O(1)

# key, value를 list로 저장하는 class
class LinkedTuple:
    def __init__(self):
        self.items = list()

    # [("asdf1", "test")] -> [("asdf2", "test33")] 가 되게!
    # .add("asdf1", "test")   -> [("asdf1", "test")]
    # .add("asdf", "test33") -> [("asdf1", "test"), ("asdf", "test33")]
    def add(self, key, value):
        self.items.append((key, value))

    def get(self, key):
        for k, v in self.items:  # 일치하는 key의 value들만
            if key == k:
                return v


# 충돌 해결 class
class LinkedDict:
    def __init__(self):
        # 기존의 데이터를 담아놓을 공간（linked list) 필요
        self.items = []
        for i in range(8):
            # [LinkedTuple(), LinkedTuple(), LinkedTuple(),,,]
            # 즉, 각 원소에 키가 동일하면 똑같은 LinkedTuple안에서 값들이 -> -> 이렇게 쭉쭉 늘어난다.
            self.items.append(LinkedTuple())  # init LinkedTuple() is empty []

    # 현재, self.items[index]에 LinkedTuple() 즉, [] 이 들어있다.
    # LinkedTuple()
    # []
    # [(key, value)] <- 우리가 하고싶은 것 == add()
    def put(self, key, value):  # key에 대한 self.items를 찾아서 value를 리턴해주는 함수
        index = hash(key) % len(self.items)
        # self.items[key % index] = value - 기존 방식
        # key % index 가 키값이 같은 것은 같은 index!
        self.items[index].add(key, value)  # items배열에서 key % index 번째에 key, value 계속 저장

    def get(self, key):
        index = hash(key) % len(self.items)
        return self.items[index].get(key)