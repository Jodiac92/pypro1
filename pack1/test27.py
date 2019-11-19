# 상속
class Person:
    say = '난 사람이야~~~'
    nai = 20
    __kbs = '공영방송' # private 멤버
    def __init__(self, nai):
        print('Person 생성자')
        self.nai = nai
        
    def printInfo(self):
        print('나이 : {}, 이야기 : {}'.format(self.nai, self.say))
        
    def Hello(self):
        print('person 안녕')
        print('Hello : ', self.say, self.__kbs)
    
    @staticmethod
    def sbs(tel):
        print('sbs method ', tel)
        
print(Person.say, Person.nai)
p = Person('22')
p.printInfo()
p.Hello()

print('---' * 20)

class Employee(Person):
    say = '일하는 동물'
    subject = '근로자'
    def __init__(self):
        print('Employee 생성자')
    
    def printInfo(self): # 오버라이딩
        print('Employee PrintInfo')
        
    def EprintInfo(self):
        self.printInfo()
        super().printInfo()
        print(self.say, super().say)
        self.Hello()
e = Employee()
print(e.say, e.nai, e.subject)
e.printInfo()
e.EprintInfo()

print('***' * 20)
class Worker(Person):
    star = 100
    def __init__(self, nai):
        print('Worker 생성자')
        super().__init__(nai) # 부모 클래스 생성사 호출 - Bound method call
    
    def WprintInfo(self):
        self.printInfo()
        super().printInfo()
w = Worker('25')
print(w.say, w.nai)
w.printInfo()
w.WprintInfo()    
    
print('^^^' * 20)

class Programmer(Worker):
    def __init__(self, nai):
        print('Programmer 생성자')
        Worker.__init__(self, nai) # UnBound method call
    
    def printInfo(self):
        print('Programmer printInfo')
        
    def PprintInfo(self):
        self.printInfo()
        super().printInfo()
        print(super().say)
        #print(super().__kbs) # err : __kbs가 private 멤버이기 때문에
pr = Programmer(26)
print(pr.say, pr.nai)
pr.PprintInfo()
pr.Hello()
pr.sbs('111-111')

print('-----------------------------------------')
a = 10; print(type(a))
print(type(pr))
print(Programmer.__bases__)
print(Person.__bases__)
