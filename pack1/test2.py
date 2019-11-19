# 연산자
v1 = 3
v1 = v2 = v3 = 5
print(v1, v2, v3, end='\t')
print('출력')
v1 = 1,2,3
print(v1)
v1, v2 = 10, 20
print(v1, v2)
v2, v1 = v1, v2
print(v1, v2)

print('\n값 할당 packing')
#*v1, v2 = 1,2,3,4,5
v1, *v2 = 1,2,3,4,5
print(v1)
print(v2)

print('출력 서식-----------------')
print(format(1.5678, '10.3f'))
print('올 해는 %d 년'%2019)
print('올 해는 %d 년 %s'%(2019, '만세'))
print('올 해는 %f년'%2019.11)
print('이름은 {}, 나이는 {}입니다'.format('홍길동', 22))
print('이름은 {0}, 나이는 {1}입니다'.format('홍길동', 22))
print('이름은 {1}, 나이는 {0}입니다'.format('홍길동', 22))

print('\n\n 연산자 연습 ----------')
print(5 + 3, 5 - 3, 5 * 3, 5 / 3, 5 // 3, 5 % 3, 5 ** 3)
print(divmod(5,3))
print('우선 순위', 3 + 4 * 5, (3 + 4) * 5)

print('관계, 논리')
print(5 > 3, 5 == 3, 5 != 3)
print(5 > 3 and 4 < 3)
print(not(5 >= 3))

print()
print('문자' + '더하기')
print('문자' * 20)

print('누적')
a = 10
a = a + 1
print(a)
a += 1
# a++;++a # 증감연산자는 사용할 수 없다
print(a)

print(a)
print(a * -1, -a, --a) # --a는 그냥 부호로 사용

print('T, F 처리 : ', bool(False),bool(0),bool(''),bool(None),bool([]))
print('T, F 처리 : ', bool(True),bool(1),bool(-1),bool(3.4),bool('a'))

print('aa\bbb')
print('aa\nbb')
print('c:\\mbc\\sbs\\abc.txt')
print(r'c:\mbc\sbs\abc.txt')