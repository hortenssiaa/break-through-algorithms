# 문자열 s가 올바른 괄호이면 True 를 반환하고 아니라면 False 를 반환하시오.
# ) : -1
# ( : +1

s = "(())()"
# s = "())()"
# s = "((())"


def is_correct_parenthesis(string):
    string_cal = 0
    stack = []

    for char in string:
        if char == '(':
            stack.append(1)
        else:
            stack.append(-1)


    stack_len = len(stack)
    for i in range(stack_len):
        string_cal += stack.pop()

        if (i == 0) and string_cal > 0:
            return False

        if (i == stack_len - 1) and string_cal != 0:
            return False

    return True


print(is_correct_parenthesis(s))  # True 를 반환해야 합니다!