import multiplication_table as mt

number = int(input('궁금한 구구단을 입력하세요 (ex : 3단이면 숫자 3만 입력.) : '))

if number == 1:
    mt.one(number)
elif number == 2:
    mt.two(number)
elif number == 3:
    mt.three(number)
elif number == 4:
    mt.four(number)
elif number == 5:
    mt.five(number)
elif number == 6:
    mt.six(number)
elif number == 7:
    mt.seven(number)
elif number == 8:
    mt.eight(number)
elif number == 9:
    mt.nine(number)
else:
    print("1과 9사이의 숫자를 입력하세요.")