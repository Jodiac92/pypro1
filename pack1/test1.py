'''
여러줄 주석
'''
from builtins import isinstance
"""
여러줄 주석
"""
# 한줄 주석
# 변수 : 참조형
var1 = '안녕파이썬'
print(var1)
var1 = 5; print(var1)
var1 = 1.5; print(var1)

a = 10; b = 20.5
c = b
print(a,b,c)
print(id(a),id(b),id(c))
c = 10
print(a is b, a == b)
print(a is c, a == c)

A = 10
a = 5
print(A, ' ', a)

print('-----------------------')
import keyword
print('키워드 목록 : ',keyword.kwlist)

print('-----------------------')
print(10, oct(10), hex(10), bin(10))
print(10, 0o12, 0xa, 0b1010)

print('type(자료형) ------------')
print(7,type(7))
print(7.1,type(7.1))
print(7 + 2j,type(7 + 2j))
print(True,type(True))
print('a',type('a')) # 'a', "a"
print()
print((1,),type((1,)))
print([1],type([1]))
print({1},type({1}))
print({'k':1},type({'k':1}))

a = 5
print(isinstance(a, int))
print(isinstance(a, list))