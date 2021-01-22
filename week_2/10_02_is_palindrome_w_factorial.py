# palindrome inspecting with factorial (회문검사)
# * Factorial
# 1. 축소시키는 개념
# 2. palindrome 검사 구현시; 문자열일 때 슬라이싱 사용할 것

input = "소주만병만주소"

def is_palindrome(string):
    # 1.처음과 끝을 비교해서 같지 않으면 return False
        # 1-1. 같다면, string[0:0] -> string[1:-1] -> string[2:-2] .. 로 축소시킨다는 것임
    # 2. 같으면, 처음과 끝 비교하는 return 으로 is_palindrome() 호출
    start = 0
    last = len(string) # string lengh : 6, [0~5] existing
    if last < 1:
        return 1

    if string[start:start+1] != string[last-1:last]: # s[5:6] -> [4:5]
        return False
    # string = string[start+1:last-1]
    is_palindrome(string[start+1:last-1])
    return True



print(is_palindrome(input))