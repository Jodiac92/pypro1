# 함수 : 

#def ShowGugu(start, end):
def ShowGugu(start, end=5):
    for dan in range(start, end + 1):
        print(str(dan) + '단 출력')
ShowGugu(2, 3)
print()
ShowGugu(3)
print()
ShowGugu(start = 2, end = 3)
print()
ShowGugu(end = 3, start = 2)
print()
ShowGugu(2, end = 3)
print()
#ShowGugu(start = 2, 3) # err
#ShowGugu(end = 3, 2) # err

print('가변 인수 처리')
def func1(*ar):
    print(ar)
    for i in ar:
        print('음식 : ' + i)

func1('김밥')
func1('김밥','공기밥','주먹밥')

print()
def func2(a,*ar):
    print(a)
    print(ar)

func2('김밥')
func2('김밥','공기밥','주먹밥')

print()
print()
def func3(a,*ar, **other):
    print(a)
    print(ar)
    print(other)
    
func3(1)
func3(1, 2, 3)
func3(1, 2, 3, k = 4, x = 5)


print('클로저' * 10)
# 함수명은 객체의 주소를 기억
def times(a, b):
    c = a * b
    return c

print(times(2, 3))
#print(c) # name 'c' is not defined
kbs = times # 주소 치환
print(kbs(2, 3))
print(id(kbs), id(times))
del times
#print(times(2, 3)) # name 'times' is not defined
print(kbs(2, 3))
sbs = kbs

print('------------------')
def out():
    count = 0
    def inn():
        nonlocal count
        count += 1
        return count
    #inn()
    print(inn())

out()

print('**'*10)
def out2():
    count = 0
    def inn2():
        nonlocal count
        count += 1
        return count
    return inn2 # 클로저

print(out2())
vv = out2()
print(vv())
print(vv())
print(vv())

vv2 = out2()
print(vv2())

print('-------수량  * 단가  * 세금 결과 출력------------')
def outer(tax):
    def inner(su, dan):
        amount = su * dan * tax
        return amount
    return inner

r1 = outer(0.1)
result = r1(5,10000)
print(result)
result = r1(10,30000)
print(result)

r2 = outer(0.05)
result2 = r2(5,10000)
print(result2)