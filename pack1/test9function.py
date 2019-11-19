# 함수 (function) : 소스의 재활용
# 내장 함수
print(sum([3,5,7]))
print(sum((3,5,7)))
print(sum({3,5,7}))
print(bin(8)) # 2진수

a = 10
b = eval('a + 5') # 문자열을 수식으로 변환
print(b)

print(round(1.2), round(1.5)) # 반올림

import math
print(math.ceil(1.2), math.ceil(1.6)) # 올림
print(math.floor(1.2), math.floor(1.6)) # 내림

print()
b_list = [True, 1, False]
print(all(b_list)) # 모두 참일 때 참
print(any(b_list)) # 하나라도 참이면 참

b_list2 = [1, 3, 2, 5, 7, 6]
result = all(a < 10 for a in b_list2)
print(result)


# ..........................................

# 사용자 정의 함수
def DoFunc1():
    print('DeFunc1 수행')
    
DoFunc1()
print(DoFunc1)

print()
def DoFunc2(arg1, arg2):
    DoFunc1()
    re = arg1 + arg2
    if re % 2 == 1:
        return 
    else:
        return re

print(DoFunc2(2, 4))

aa = DoFunc2(10,4)
bb = DoFunc2(10,3)
print(aa)
print(bb)
print('현재 모듈의 객체 목록', globals())

print()
def SwapFunc(a,b):
    return b, a

print(SwapFunc(3, 4))
print(SwapFunc('a', 'b'))

def isOdd(arg):
    return arg % 2 == 1
print(isOdd(2))
print(isOdd(3))

mydit = {x:x * x for x in range(11) if isOdd(x)}
print(mydit)

