# 파일 읽기/저장

import os
print(os.getcwd())

try:
    print('파일 읽기')
    f1 = open('abc.txt', mode = 'r', encoding = 'utf-8') # r, w, a +b...
    print(f1)
    print(f1.read())
    f1.close()
    
    print('파일 저장')
    f2 = open('aaa.txt', mode = 'w', encoding = 'utf-8')
    f2.write('안녕 친구\n')
    f2.write('금요일이야\n')
    f2.close()
    print('저장 성공')
    
    print('파일 추가')
    f3 = open('aaa.txt', mode = 'a', encoding = 'utf-8')
    f3.write('\n 대영')
    f3.write('\n 희원')
    f3.write('\n 막내')
    f3.close()
    print('추가 성공')
    
    print('파일 읽기')
    f4 = open('aaa.txt', mode = 'r', encoding = 'utf-8')
    print(f4.readline())
    print(f4.readline())
    f4.close()
except Exception as e:
    print('err :', e)

#--- with 블럭 : 내부적으로 close()------------
import pickle
try:
    with open('aaa.txt', mode = 'r', encoding = 'utf-8') as f5:
        print(f5.read())
        
    print('피클링 - 복합객체 처리 ---')
    '''
    dicdata = {'tom' : '111-1111', '길동' : '222-2222'}
    listdata = ['마우스', '키보드']
    tudata = (dicdata, listdata)
    
    with open('coffee.dat', 'wb') as f6:
        pickle.dump(tudata,f6)
        pickle.dump(listdata,f6)
    print('저장 완료')
    '''
    
    print('피클 객체 읽기')
    with open('coffee.dat', 'rb') as f7:
        a, b = pickle.load(f7)
        print(a)
        print(b)
        print()
        c = pickle.load(f7)
        print(c)
except Exception as e2:
    print('err :',e2)