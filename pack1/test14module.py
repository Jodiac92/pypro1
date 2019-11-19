# Module : 명령문, 함수, 클래스 등으로 구성된다


a = 10
print('뭔가를 진행')

import sys
print('모듈 경로 : ', sys.path)

#sys.exit() # 프로그램 강제 종료
print('프로그램 종료')

#from math import pi
#print(pi)
import math
print(math.pi)
print(math.sin(math.radians(30)))

import calendar
calendar.setfirstweekday(6)
print()
calendar.prmonth(2019,11)
del calendar

import os
print(os.getcwd())
print(os.listdir('./'))

print()

import random
print(random.random())
print(random.randrange(1,10))

#from random import random # from 모듈 import 멤버변수, 멤버함수
#print(random())

from random import *
print(random())
