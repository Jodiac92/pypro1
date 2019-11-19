# while

a = 1
while a <= 5:
    print(a, end = ' ')
    a += 1
    
print('end')

i = 1
while i <= 3:
    j = 1
    while j <= 4:
        print('i=' + str(i) + ' / j=' + str(j))
        j = j +1
    i = i + 1
    
print('1~ 100 사이의 3의 배수의 합')
i = 1; hap = 0
while i <= 100:
    if i % 3 == 0:
        hap += i
    i += 1  
print('합은' + str(hap))

print()
colors = ['r', 'g', 'b']
a = 0
while a < len(colors):
    print(colors[a], end = ' ')
    a += 1

print()
i = 1
while i <= 10:
    j = 1
    re = ''
    while j <= i:
        re += '*'
        j += 1
    print(re)    
    i += 1
    
# 문1) 1 ~ 100 사이의 숫자중 3의 배수 이나 2의 배수가 아닌 수를 출력하고 그들의 합을 구하시오
i, sum = 1, 0
while i <= 100:
    if i % 3 == 0:
        if i % 2 != 0:
            print(i, end=', ')
            sum += i
    i += 1
print('\n합 : ' + str(sum))

# 문2) -1, 3, -5, 7, -9, 11 ~ 99 까지의 합을 구하시오
i, j, sum = 1, 1, 0
while i < 100:
    if i % 2 != 0:
        j *= -1
        sum += (i * j)
    i += 1
print(sum)

# 문3) 1 ~ 1000 사이의 소수 ( 1보다 크고 1과 자신의 수 이외에는 나눌 수 없는 수)
i, sum, count = 1, 0, 0
while i <= 1000:
    j = 2
    while j <= i:
        if i % j == 0:
            if i != 1:
                break
        j += 1
    if i == j:
        print(i, end=', ')
        count += 1
        sum += i
    i += 1
print('\n갯수: ' + str(count))
print('합 : ' + str(sum))

print()

import time

sw = input('스위치 온[y|n]')

if sw == 'y' or sw == 'Y':
    count = 5
    while 1 <= count:
        print('%d초 남았어요!'%count)
        time.sleep(1)
        count -= 1
    print('폭발')
elif sw == 'n' or sw == 'N':
    print('작업취소')
else:
    print('y 또는 n을 누르시오')