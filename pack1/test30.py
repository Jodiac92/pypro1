from abc import *
class Employee(metaclass = ABCMeta):
    def __init__(self, irum, nai):
        self.irum = irum
        self.nai = nai
    @abstractmethod
    def pay(self):
        pass
    @abstractmethod
    def data_print(self):
        pass
    def irumnai_print(self):
        print('이름 : {}, 나이 : {},'.format(self.irum,self.nai), end = ' ')
        
class Temporary(Employee):
    def __init__(self, irum, nai, ilsu, ildang):
        super().__init__(irum, nai)
        self.ilsu = ilsu
        self.ildang = ildang
        
    def pay(self):
        return self.ilsu * self.ildang
    
    def data_print(self):
        super().irumnai_print()
        print('월급 :',self.pay())

class Regular(Employee):
    def __init__(self, irum, nai, salary):
        super().__init__(irum, nai)
        self.salary = salary
        
    def pay(self):
        return self.salary
    
    def data_print(self):
        super().irumnai_print()
        print('급여 :',self.pay())
        
class Salesman(Regular):
    def __init__(self, irum, nai, salary, sales, commossion):
        super().__init__(irum, nai, salary)
        self.sales = sales
        self.commossion = commossion
    
    def pay(self):
        return int(self.salary + (self.sales * self.commossion))
    
    def data_print(self):
        super().irumnai_print()
        print('수령액 :',self.pay())

t = Temporary('홍길동',25,20,15000)
r = Regular('한국인',27,3500000)
s = Salesman('손오공', 29, 1200000, 5000000, 0.25)

t.data_print()
r.data_print()
s.data_print()
