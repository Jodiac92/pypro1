# try ~ except 예외 처리
def divide(a, b):
    return a / b

print('어쩌구저쩌구 ...')
'''
c = divide(5, 2)
#c = divide(5, 0) # err
print(c)
'''

try:
    c = divide(5, 2)
    #c = divide(5, 0)
    print(c)
    
    aa = [1, 2]
    print(aa[1])
    
except ZeroDivisionError:
    print('나누기 오류')
except IndexError as e:
    print('참조 범위 오류 :', e)
except Exception as err:
    print('에러 발생 :', err)
finally:
    print('언제나 수행')
print('다음 작업 계속')