# singleton

class MySingle:
    inst = None
    
    def __new__(cls):
        if cls.inst is None:
            cls.inst = object.__new__(cls)
        return cls.inst
    
    def aa(self):
        print('내 메소드')
        
class Sub(MySingle):
    pass

s1 = Sub()
s2 = Sub()
print(id(s1), id(s2))

s1.aa()
s2.aa()

print('사용 가능한 멤버 고정 ------------')
class Animal:
    __slots__ = ['name','age'] # 멤버 필드 고정
    
    def printData(self):
        print(self.name, self.age)
        
        
ani = Animal()
ani.name = 'tiger'
ani.age = 3
print(ani.name + ' ' + str(ani.age))
ani.printData()
ani.abc = 10