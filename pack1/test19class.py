# 클래스 : 상속(다형성), 포함 등의 기법 구사
print('어쩌구 저쩌구 하다가.........')

class TestClass:
    aa = 1 # 멤버 변수(클래스 내 전역변수)
    
    def __init__(self):
        print('생성자')
        
    def __del__(self):
        print('소멸자')
    
    # 메소드
    def printMsg(self):
        name = '홍길동'
        print(name)
        print(self.aa)
    
test = TestClass() # 생성자 호출
print(test.aa)
# print(type(test))
# a = 1
# print(type(a))
print(TestClass.aa)

print('메소드 호출---------')
test.printMsg() # Bound method call
TestClass.printMsg(test) # UnBound method call
print(id(test), id(TestClass))