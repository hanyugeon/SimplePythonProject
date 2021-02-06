# 대문자 소문자를 출력한다.
# capital method : .upper, .capitalize, .title
def capitalize(demo):
    mod = str()
    print(mod.upper())
    mod = demo
    print(mod.lower())


# 대소문자를 서로 바꾼다.
def switching_up_low(demo):
    mod = str()
    for c in demo:
        if c.islower():
            mod += c.upper()
        else:
            mod += c.lower()
    print(mod)
    print()


# 문자열이 10자 이상이면 5번째와 10번째 문자의 위치를 바꾸고 출력
def switch_5_10(demo):
    mod = str()
    if len(demo) >= 10:
        mod = str()
        mod += demo[0:4]
        mod += demo[9]
        mod += demo[5:9]
        mod += demo[4]
        mod += demo[10:]
    print(mod)
    print()

# 반복되는 문자열은 제거한다.
def del_overlap(demo):
    mod = str()
    for i in range(len(demo) - 1):
        if demo[i] != demo[i + 1]:
            mod += demo[i]
    mod += demo[-1]
    print(mod)
    print()

# 마지막으로 순서를 뒤집어서 출력
def reverse_str(demo):
    mod = demo
    print(mod.swapcase())