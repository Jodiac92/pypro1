class Machine:
    def __init__(self):
        self.CoinIN = CoinIN();
        
    def showData(self):
        self.CoinIN.coin = input("동전을 입력하시오 : ")
        self.cupCount = input("몇 잔을 원하세요 : ")
        self.CoinIN.culc(self.cupCount)
        if self.CoinIN.change < 0:
            print('잔액이 부족합니다')
        elif self.CoinIN.change == 0:
            print('커피 {}잔 입니다.'.format(self.cupCount))
        else:
            print('커피 {}잔과 잔돈 {}원 입니다'.format(self.cupCount,self.CoinIN.change))
        
class CoinIN:
    def __init__(self):
        self.coin = 0
        
    def culc(self, cupCount):
        self.change = int(self.coin) - 200 * int(cupCount)
            
if __name__ == '__main__':
    Machine().showData()