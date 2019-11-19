# class
class Car:
    handle = 0
    speed = 0
    
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        
    def showData(self):
        km = '킬로미터'
        msg = '속도 : ' + str(self.speed) + km
        return msg
    
print(Car.handle)
#Car.showData()

car1 = Car('tom',10)
print(car1.handle, car1.name, car1.speed)
car1.color = '검정' # car1객체에 멤버 추가, 원형에는 멤버 추가 X
print(car1.color)

print()

car2 = Car('james', 20)
print(car2.handle, car2.name, car2.speed)
#print(car2.color) # 'Car' object has no attribute 'color'
#print(Car.color) # type object 'Car' has no attribute 'color'

print('주소 출력')
print(id(Car), id(car1), id(car2))
print(car1.__dict__)
print(car2.__dict__)

print('method ----------------')
print('car1',car1.showData())
print('car2',car2.showData())