# 클래스의 상속 - 다형성을 구현
class Animal:
    def __init__(self):
        print('Animal 생성자')
        
    def move(self):
        print('움직이는 생물')

#-------------------------------

class Dog(Animal): # 상속
    def my(self):
        self.move()
        print('나는 개')
        
dog1 = Dog()
dog1.my()

print()

class Horse(Animal):
    pass
 
hor1 = Horse()
hor1.move()