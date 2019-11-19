# while

a = 0

while a < 10:
    a += 1
    if a == 5: continue
    if a == 7: break
    print(a)
else:
    print('while 수행')
    
print('while 수행  후  %d'%a)

import random

num = random.randint(1,10)
#print(num)

while True:
    print('1 ~ 10 사이이 컴이 가진 수를 입력')
    guess = input()
    su = int(guess)
    if su == num:
        print('성공 ' * 5)
        break
    elif su > num:
        print('더 작은 수 입력')
    elif su < num:
        print('더 큰 수 입력')