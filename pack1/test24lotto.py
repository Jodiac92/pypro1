# 로또 번호 출력기
import random
class LottoBall:
    def __init__(self, num):
        self.num = num
        
class LottoMachine:
    def __init__(self):
        self.ballList = []
        for i in range(1,46):
            self.ballList.append(LottoBall(i)) # 포함
            
    def selectBalls(self):
        # 섞기 전
        for a in range(45):
            print(self.ballList[a].num, end = ' ')
        print()
        random.shuffle(self.ballList)
        for a in range(45):
            print(self.ballList[a].num, end = ' ')
        print()
        return self.ballList[0:6]
    
class LottoUi:
    def __init__(self):
        self.machine = LottoMachine() # 포함
        
    def playLotto(self):
        input("로또 번호를 얻기 위해서 키를 누르시오")
        selectedBalls = self.machine.selectBalls()
        for ball in selectedBalls:
            print('%d '%ball.num, end = ' ')
            
if __name__ == '__main__':
    LottoUi().playLotto()