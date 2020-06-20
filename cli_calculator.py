"""
어떤 로직으로 구현할 것인가?
1. user_input = "5+5*10" 이 들어왔다면, 숫자와 연산 기호를 각각 분리해서 각각 리스트화 시킨다.
"""
operator = ["+", "-", "*", "/", "="]

def string_calculator(user_input):
    string_list = []
    lop = 0

    if user_input[-1] not in operator:
        user_input += "="

    for i, s in enumerate(user_input): #enumerate를 사용하여 Index 번호까지 가져오기
        if s in operator:
            if user_input[lop:i].strip() != "":
                string_list.append(user_input[lop:i])
                string_list.append(s)
                lop = i + 1

    string_list = string_list[:-1]

    pos = 0
    while True:
        if pos + 1 > len(string_list):
            break
        if len(string_list) > pos + 1 and string_list[pos] in operator:
            temp = string_list[pos - 1] + string_list[pos] + string_list[pos + 1]
            del string_list[0:3]
            string_list.insert(0, str(eval(temp)))
            pos = 0
        pos += 1
    if len(string_list) > 0:
        result = float(string_list[0])

    return round(result, 4)

while True:
    user_input = input("계산식을 입력하세요> ")
    if user_input == "exit":
        break
    result = string_calculator(user_input)
    print("결과: {}".format(result))
