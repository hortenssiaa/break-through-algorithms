'''
parti : ["leo", "kiki", "eden"]
comp : ["leo", "kiki"]
'''

# 처음 풀이
participant = ["eden", "leo", "kiki", "leo"]
completion = ["leo", "kiki"]

def solution(participant, completion):
    for winner in completion:
        for person in participant:
            if winner == person:
                participant.remove(person)
                break
    answer = participant[0]
    return answer

# print(solution(participant, completion))




# 문제 풀이 - 해시인거 알고 다시 풀어보기
# 해시
# 문자열 이름을, 번호라고 생각하기

# participant = ["eden", "leo", "kiki", "leo"]
# completion = ["leo", "kiki"]
participant = ["m", "s", "m", "a"]
completion = ["s", "a", "m"]

data = dict()
def solution2(participant, completion):
    answer = ""
    for person in participant:
        data[person] = participant.count(person)

    for person in participant:
        if data[person] == 2:
            answer = person
            break

    return answer

print(solution2(participant, completion))




# 문제 풀이 - 답지
# 해시
