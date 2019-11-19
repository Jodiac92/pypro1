# 모듈의 멤버들
kor = 100

def abc():
    print('함수')
    
class My:
    #kor = 90
    
    def abc(self):
        print('메소드')
    def show(self):
        #kor = 80
        print(kor)
        #print(self.kor)
        self.abc()
        abc()
my = My()
my.show()

print('----------------')
class My2:
    a = 1
    
print(My2.a)

aa = My2()
print(aa.a)
aa.a = 2
print(aa.a)

print()
bb = My2()
print(bb.a)
bb.a = 3
print(bb.a)
bb.b = 4
print(bb.b)
print()
print(My2.a)
print(aa.a)
print(bb.a)
#print(My2.b) # err
#print(aa.b) # err

print('클래스는 새로운 type 생성')
class Singer:
    title_song = '화이팅 코리아'
    
    def sing(self):
        msg = '노래는 '
        print(msg, self.title_song)
        
psy = Singer()
psy.sing()

print()
girls = Singer()
girls.sing()
girls.title_song = '가을예찬'
girls.sing()
girls.co = 'sm'
print('girls 소속사 ',girls.co)

print()
psy.sing()
#print('psy 소속사 ',psy.co) # err




