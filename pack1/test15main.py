# 사용자 정의 모듈 연습
import pack1.mymod1

print('모듈 연습')

def func():
    print('현재 모듈의 함수 수행')
    
func()

print()
print('tot',pack1.mymod1.tot)
from pack1.mymod1 import tot
print('tot', tot)

pack1.mymod1.myfunc(pack1.mymod1.tot)
pack1.mymod1.kbs()
pack1.mymod1.mbc()

print()
from pack1.mymod1 import kbs, mbc, myfunc
#from pack1.mymod1 import *
myfunc(7)
   
if __name__ == '__main__':
    print('여기가 메인 모듈')
    
print('다른 패키지의 모듈 참조')

import other.mymod2
print(other.mymod2.Cha(10, 3))
print(other.mymod2.hap(10, 3))

print('경로 설정된 폴더에 모듈 읽기')
from mymod3 import Gop
print(Gop(3,4))