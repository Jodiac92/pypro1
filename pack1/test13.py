# 함수 장식자 : meta 기능을 가짐
# 다른 함수를 감싸는 기능

def make2(fn):
    return lambda:'안녕' + fn()

def make1(fn):
    return lambda:'반가워' + fn()

def hello():
    return '홍길동'

hi = make2(make1(hello))
print(hi())

print('---------------------------------------')
@make2
@make1
def hello2():
    return '신기해'

print(hello2())

print('------재귀함수-----------')
def CountDown(n):
    if n == 0:
        print('완료')
    else:
        print(n, end = ' ')
        CountDown(n - 1) # 재귀함수
    
CountDown(5)

print()
def tot_func(n):
    if n == 1:
        print('탈출')
        return True
    return n + tot_func(n - 1)

result = tot_func(10)
print('합은 : ',result)