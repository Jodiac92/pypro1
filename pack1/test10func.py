# 변수의 생존 범위
# 변수 영역 및 접근 순서 Local > Enclosing function > Global

player = '전국대표' # 전역변수(Global)

def funcSoccer():
    name = '홍길동' # 지역변수(Local)
    player = '지역대표'
    print(name,player)

funcSoccer()

print()
a = 10; b = 20; c = 30
def Foo():
    a = 40; b = 50; c = 70
    def Bar():
        #c = 60
        global c
        nonlocal b
        print('지역1: a:{}, b:{}, c:{}'.format(a,b,c))
        c = 60 # local variable 'c' referenced before assignment
        b = 80
    Bar()
    print('지역2: a:{}, b:{}, c:{}'.format(a,b,c))
Foo()    
print('전역 : a:{}, b:{}, c:{}'.format(a,b,c))