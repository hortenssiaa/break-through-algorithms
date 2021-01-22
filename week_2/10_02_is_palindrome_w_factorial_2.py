# palindrome inspecting with factorial (회문검사)
# * Factorial
# 1. 축소시키는 개념
# 2. palindrome 검사 구현시; 문자열일 때 슬라이싱 사용할 것 

input = "소주만병만주소d"
"주만병만주"
"만병만"
"병"

def is_palindrome(string):
    if string[0] != string[-1]:  # string은 계속 짧아지니, [0], [-1]로 계속 비교 가능
        return False
    if len(string) <= 1:  # 문자가 하나일 때
        return True
    return True

print(is_palindrome(input))