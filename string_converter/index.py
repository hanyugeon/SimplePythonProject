# 문자열 가지고 놀기
import string_converter as sc

# 문자열을 입력받는다.
demo = str(input('문자열을 입력하세요 : '))
mod = demo
print(demo)
print()

# 대문자 소문자를 출력한다.
# capital method : .upper, .capitalize, .title
sc.capitalize(demo)

# 대소문자를 서로 바꾼다.
sc.switching_up_low(demo)

# 문자열이 10자 이상이면 5번째와 10번째 문자의 위치를 바꾸고 출력
sc.switch_5_10(demo)

# 반복되는 문자열은 제거한다.
sc.del_overlap(demo)

# 마지막으로 순서를 뒤집어서 출력
sc.reverse_str(demo)