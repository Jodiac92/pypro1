# 추상 클래스
from abc import *

class AbstractClass(metaclass = ABCMeta):
    def __init__(self):
        print('생성자')
        
    def nomalMethod(self):
        print('추상클래스 내의 일반 메소드')

    @abstractmethod
    def absMethod(self): # 추상 메소드
        pass
    
#parent = AbstractClass() # Can't instantiate abstract class

class Child1(AbstractClass):
    name = '난 Child1'
    
    def absMethod(self):
        print('추상 메소드를 오버라이딩')

class Child2(AbstractClass):
    name = '난 Child2'
    
    def absMethod(self):   
        print('추상 메소드를 여전히 오버라이딩')
    
    def nomalMethod(self):
        print('추상클래스 내의 일반 메소드를 재정의 : 선택')
        
c1 = Child1()
print(c1.name)
c1.absMethod()
c1.nomalMethod()
print()
c2 = Child2()
print(c2.name)
c2.absMethod()
c2.nomalMethod()