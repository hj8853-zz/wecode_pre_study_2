def plus(a,b):
    return a+b

def minus(a,b):
    return a-b

def multiply(a,b):
    return a*b

def div(a,b):
    return a/b

while True:
    print("="*100)
    print("계신식을 선택하세요. > 1.덧셈 2.뺄셈 3.곱셈 4.나눗셈 5.종료")
    print("="*100)
    select_number = int(input())
    if select_number <= 4:
        first = int(input("첫번째 숫자를 입력해주세요 > "))
        second = int(input("두번째 숫자를 입력해주세요 > "))
        if select_number == 1:
            result = first+second
            print("결과: {}".format(result))
        elif select_number == 2:
            result = first-second
            print("결과: {}".format(result))
        elif select_number == 3:
            result = first*second
            print("결과: {}".format(result))
        elif select_number == 4:
            result = first/second
            print("결과: {}".format(result))
    elif select_number == 5:
        break
    else:
        print("1~5 사이의 수를 입력해주세요.")
    