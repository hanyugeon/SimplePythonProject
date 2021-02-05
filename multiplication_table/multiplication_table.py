# 구구단 결과를 불러오는 함수를 적는다.
# import를 활용하여 index.py 에 호출시킬것.
# 자주일어나는 일은 간단 명료하게.

def multiply(n):
    while n < 1 or n > 9:
        print('오류 : 1과 9 사이의 숫자를 입력하세요')
        n = int(input('구구단을 외자~ (숫자입력) :'))
    for m in range(1, 10):
        print('%d x %d = %d' % (n, m, n * m))


# def main():
#     print("Testing mt.one function")
#
#     test_number = 1
#     one(test_number)
#
#     print("test is end!")
#
# if __name__='__name__':
#     main()