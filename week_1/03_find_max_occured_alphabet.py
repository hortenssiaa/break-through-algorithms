input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    alphabet_occurency_array = [0]*26
    for char in string:
        if not char.isalpha():
            continue
        else:
            alphabet_occurency_array[ord(char)-ord('a')] += 1

    max_occurrece = 0 # 빈도수
    max_alpha_index = 0 # 가장 많이 나온 알파벳의 index

    for index in range(len(alphabet_occurency_array)):
        if max_occurrece < alphabet_occurency_array[index]:
            max_occurrece = alphabet_occurency_array[index]
            max_alpha_index = index
    return chr(max_alpha_index + ord('a'))

result = find_max_occurred_alphabet(input)
print(result)