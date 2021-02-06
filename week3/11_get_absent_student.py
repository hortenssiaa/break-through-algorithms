all_students = ["나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"]
present_students = ["정연", "모모", "채영", "쯔위", "사나", "나연", "미나", "다현"]

# test_arr = [None] * len(all_students)
# count = 0
# for name in all_students:
#     test_arr[hash(name) % len(all_students)] = count
#     count += 1
#
# print(test_arr)
#
# for name in all_students:
#     print(f'{name} : {test_arr[hash(name) % len(all_students)]}')

t1 = ['a', 'b', 'c', 'd', 'e']
t2 = ['a', 'b']

class LinkedTuple:
    def __init__(self):
        self.items = list()

    def add(self, key, value):
        self.items.append((key, value))

    def get(self, key):
        for k, v in self.items:
            if key == k:
                return v
        else:
            return None

# 충돌 해결 class
class LinkedDict:
    def __init__(self, array):
        self.items = []
        for i in range(len(array)):
            self.items.append(LinkedTuple())

    def put(self, key, value):
        index = hash(key) % len(self.items)
        self.items[index].add(key, value)

    def get(self, key):
        index = hash(key) % len(self.items)
        return self.items[index].get(key)


# test = LinkedDict(t2)
# store = []
# test.put('a', 'v1')
# test.put('b', 'v2')
# for key in t1:
#     if test.get(key) is None:
#         store.append(key)
#
# print(store)

def get_absent_student(all_array, present_array):
    likedict = LinkedDict(present_array)
    absent_student = []

    for key_name in present_array:  # O(N)
        likedict.put(key_name, 0)

    for key_name in all_array:  # O(N)
        if likedict.get(key_name) is None:
            absent_student.append(key_name)

    return absent_student


print(get_absent_student(all_students, present_students))