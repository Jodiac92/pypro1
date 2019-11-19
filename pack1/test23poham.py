# 냉장고 클래스에 음식 클래스 담기
class Fridge:
    isOpened = False
    food = []
    
    def open(self):
        self.isOpened = True
        print('냉장고 문 열기')
        
    def put(self, thing):
        if self.isOpened:
            self.food.append(thing) # 포함
            print('냉장고 속에 음식 저장')
            self.list()
        else:
            print('냉장고 문이 닫혀 음식을 담을 수 없음')
    def list(self):
        for f in self.food:
            print('-', f.irum, f.expiry_data)
        print()
        
    def close(self):
        self.isOpened = False
        print('냉장고 문 닫기')
    
# ---------------------------------------------    
class FoodData:
    def __init__(self, irum, expiry_data):
        self.irum = irum
        self.expiry_data = expiry_data
        
# ---------------------------------------------
f = Fridge()
apple = FoodData('사과','2019-11-17')
f.open()
f.put(apple)
f.close()

print()
coke = FoodData('콜라','2020-11-17')
f.open()
f.put(coke)
f.close()