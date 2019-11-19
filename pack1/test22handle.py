# 핸들 클래스 : 다른 클래스에서 사용을 목적
class PohamHandle:
    quantity = 0 # 회전량
    
    def LeftTurn(self, quantity):
        self.quantity = quantity
        return '좌회전'
    def RightTurn(self, quantity):
        self.quantity = quantity
        return '우회전'
    