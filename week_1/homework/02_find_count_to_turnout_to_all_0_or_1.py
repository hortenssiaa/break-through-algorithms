input = "0001100100110"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    count_number1_chainging = 1
    count_number2_chainging = 0

    init = number1 = string[0]
    number2 = '0'

    for index in range(len(string)):
        if number1 != string[index]: # string[0]와 string[index]가 다를 때 : 0->1
            number1 = string[index]
            if number1 != init:
                count_number2_chainging += 1
                next_of_init = number2 = number1

        if index > 0:
            if number2 != string[index]:
                number2 = string[index]
                if number2 != next_of_init:
                    count_number1_chainging += 1

    if count_number2_chainging == 0:
        return 1

    # print(f'{init}->{next_of_init} : {count_number1_chainging}, '
    #       f'{next_of_init}->{init} : {count_number2_chainging}')

    if count_number1_chainging <= count_number2_chainging:
        return count_number1_chainging
    else:
        return count_number2_chainging

result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)