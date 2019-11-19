# if

var = 5
if var >= 3:
    print('크구나')
    print('참')
else:
    print('거짓')

print('end1')

print()
jumsu = 85
if jumsu >= 90:
    print('수')
else:
    if jumsu >= 70:
        print('보통')
    else:
        print('저조')
        
if jumsu >= 90:
    print('우수')
elif jumsu >= 70:
    print('보통')
else:
    jumsu('저조')
    
#jum = int(input('점수 입력 : '))
jum = 77

if 90 <= jum <= 100:
    grade = '우수'
elif 70<= jum < 90:
    grade = '보통'
else:
    grade = '저조'
    
print(grade)

names = ['tom','james','oscar']
if 'james' in names:
    print('내친구')
else:
    print('네친구')

a = 'kbs'
b = 9 if a == 'kbs' else 11
print(b)

a = 11
b = 'mbc' if a == 9 else 'kbc'
print(b)

print()
a = 3
if a > 5:
    re = a * 2
else:
    re = a + 2
print(re)

print()
re = a * 2 if a > 5 else a + 2
print(re)

a = 3
print((a + 2, a * 2)[a > 5])