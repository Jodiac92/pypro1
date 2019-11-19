# 일급 함수: 함수 안에 함수 선언, 인자로 함수 전달, 반환값이 함수

def func1(a, b):
    return a + b

func2 = func1
print(func1(3, 4))
print(func2(3, 4))

def func3(f):
    def func4():
        print('나는 내부 함수야~~')
    func4()
    return f

mbc = func3(func1)
print(mbc(3, 4))

print('Lambda - 이름이 없는 한 줄 짜리 함수')

def hap(x, y):
    return x + y
print(hap(1, 2))

print((lambda x, y:x + y)(1, 2))
gg = lambda x, y : x * y
print(gg(3,4))

print()
kbs = lambda a, su = 10 : a + su
print(kbs(5))

print()
mbc = lambda a, *tu, **di : print(a, tu, di)
mbc(1, 2, 3, m = 4, n = 5)

print()
li = [lambda a, b : a + b, lambda a, b: a * b]
print(li[0](3, 4))
print(li[1](3, 4))

print('함수의 인자로 람다를 사용')
#filter(함수, 집합형)

print(list(filter(lambda a : a < 5, range(10))))
print(list(filter(lambda a : a % 2, range(10))))
