# Just Merging

array1 = [1, 2, 3, 5]
array2 = [4, 6, 7, 8]

# array_c = []
# a_index = 0
# b_index = 0
#
# for i in range(4*4):
#     if a_index >= len(array_a):
#         for b in range(b_index, len(array_b)):
#             array_c.append(array_b[b])
#         break
#     elif b_index >= len(array_b):
#         for a in range(a_index, len(array_a)):
#             array_c.append(array_a[a])
#         break
#
#     while (a_index >= len(array_a) or b_index >= len(array_b)) is not True:
#         if array_a[a_index] < array_b[b_index]:
#             array_c.append(array_a[a_index])
#             a_index += 1
#         elif array_b[b_index] < array_a[a_index]:
#             array_c.append(array_b[b_index])
#             b_index += 1
# print(array_c)

def merge(array1, array2):
    array1_index = 0
    array2_index = 0
    array_c = []

    for i in range(len(array1) * len(array2)):
        if array1_index >= len(array1):
            for b in range(array2_index, len(array2)):
                array_c.append(array2[b])
            break
        elif array2_index >= len(array2):
            for a in range(array1_index, len(array1)):
                array_c.append(array1[a])
            break

        while (array1_index >= len(array1) or array2_index >= len(array2)) is not True:
            if array1[array1_index] < array2[array2_index]:
                array_c.append(array1[array1_index])
                array1_index += 1
            elif array2[array2_index] < array1[array1_index]:
                array_c.append(array2[array2_index])
                array2_index += 1

    return array_c


print(merge(array1, array2))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!