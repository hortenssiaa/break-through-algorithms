# input = "abaaabazde"
input = "abacabade"

# O(N)
def find_not_repeating_character(string):
    alphabet_occurence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        else:
            alphabet_occurence_array[ord(char)-ord('a')] += 1

    not_repeting_first_char = []
    for index in range(len(alphabet_occurence_array)):
        if alphabet_occurence_array[index] == 1:
            not_repeting_first_char.append(chr(ord('a')+index))

    for char in string:
        if char in not_repeting_first_char:
            return char

    return '_'

result = find_not_repeating_character(input)
print(result)