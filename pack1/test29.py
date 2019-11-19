# 다중상속
class Tiger:
    data = '호랑이 만세'
    
    def cry(self):
        print('호랑이 어흥')
        
    def eat(self):
        print('맹수는 늘 고기 먹음')
        
class Lion:
    def cry(self):
        print('으르렁')
        
    def hobby(self):
        print('백수의 왕은 무한 리필 즐김')
        
class Liger1(Tiger, Lion):
    pass

a1 = Liger1()
a1.cry()
a1.eat()
print(a1.data)
a1.hobby()

print('^^^'*20)
class Liger2(Lion, Tiger):
    data = '라이거 만세'
    def play(self):
        print('라이거 고유 메소드')
        self.display()
        
    def hobby(self):
        print('라이거 취미')  

    def display(self):
        print(self.data)
        print(super().data)
        self.hobby()
        super().hobby()
        
a2 = Liger2()
a2.cry()
a2.play()