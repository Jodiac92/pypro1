class Animal:
    def move(self):
        pass
    
class Dog(Animal):
    name = '개'
    
    def move(self):
        print('Dog Move')
        
class Cat(Animal):
    name = '고양이'
    
    def move(self):
        print('Cat Move')
        
class Wolf(Dog, Cat):
    pass

class Fox(Cat, Dog):
    def move(self):
        print('Fox Move')
        
    def foxMethod(self):
        print('foxMethod')