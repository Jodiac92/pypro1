# method overriding
class Parent:
    def printData(self):
        pass
    
class Child1(Parent):
    def printData(self):
        print('Child1에서 override')
        
class Child2(Parent):
    def printData(self):
        print('Child2에서 override')
        print('부모 메소드 재정의')
    def aa(self):
        print('Child2의 일반 메소드')
c1 = Child1()
c1.printData()

print()

c2 = Child2()
c2.printData()
print("---------------------다형성---------------")
par = Parent()
par = c1
par.printData()
par = c2
par.printData()
par.aa()
print('----------------------------------------')
kbs = c1
kbs.printData()
kbs = c2
kbs.printData()

