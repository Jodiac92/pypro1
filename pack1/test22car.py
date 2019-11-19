# 메인 모듈 : PohamHandle을 현재 클래스에 포함관계로 읽기
from pack1.test22handle import PohamHandle

class PohamCar:
    turnShow = '정지'
    
    def __init__(self, ownerName):
        self.ownerName = ownerName
        # 자동차의 각종 부품 중 핸들을 읽기
        self.handle = PohamHandle() # 클래스의 포함관계
        
    def turnHandle(self, q):
        if q > 0:
            self.turnShow = self.handle.RightTurn(q)
        elif q < 0:
            self.turnShow = self.handle.LeftTurn(q)
        else:
            self.turnShow = '직진'
            
if __name__ == '__main__':
    tom = PohamCar('톰')
    tom.turnHandle(30)
    print(tom.ownerName + '의 회전량은 ' + tom.turnShow + str(tom.handle.quantity))
    tom.turnHandle(0)
    print(tom.ownerName + '의 회전량은 ' + tom.turnShow)
    print()
    oscar = PohamCar('오스카')
    oscar.turnHandle(-20)
    print(oscar.ownerName + '의 회전량은 ' + oscar.turnShow + str(oscar.handle.quantity))