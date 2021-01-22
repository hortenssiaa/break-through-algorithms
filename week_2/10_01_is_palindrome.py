# palindrome inspecting (회문검사)

input = "tomato"

def is_palindrome(string):
    left_index = 0
    right_indx = len(string) - 1

    while left_index <= right_indx:
        if string[left_index] != string[right_indx]:
            return False
        left_index += 1
        right_indx -= 1

    return True



print(is_palindrome(input))