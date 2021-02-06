# 해쉬 테이블 : 시간은 극대화 시킬 수 있되, 공간을 많이 사용하는 자료구조다!
# 해쉬 테이블(Hash Table)은
# "키" 와 "데이터"를 저장함으로써 즉각적으로 데이터를 받아오고 업데이트하고 싶을 때 사용하는 자료구조입니다.
# 해쉬 함수(Hash Function)는
# 임의의 길이를 갖는 메시지를 입력하여 고정된 길이의 해쉬값을 출력하는 함수입니다.

all_students = ["나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"]
present_students = ["정연", "모모", "채영", "쯔위", "사나", "나연", "미나", "다현"]

def get_absent_student(all_array, present_array):
    student_dic = {}
    for key_name in all_array:  # O(N)
        student_dic[key_name] = True  # 공간복잡도도 O(N)

    for key_name in present_array:  # O(N)
        del student_dic[key_name]

    # 1명 결석 시
    for key in student_dic.keys():
        return key

    # 2명이상 결석
    # return list(student_dic.keys())

print(get_absent_student(all_students, present_students))