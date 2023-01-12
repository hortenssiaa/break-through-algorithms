'''
parti : ["leo", "kiki", "eden"]
comp : ["leo", "kiki"]
'''

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

print(solution(participant, completion))