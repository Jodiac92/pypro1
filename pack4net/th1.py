# process : 실행중인 프로그램을 말함. 프로레스 고유의 메모리 점유.
# thread : 하나의 프로세스 내에서 진행되는 작은 실행 단위

from subprocess import *
# Popen('c:/windows/system32/calc.exe') # 응용 프로그램 실행(다음 문장 실행)
# print('계산기 수행')
# call('c:/windows/system32/notepad.exe') # 응용 프로그램 실행(다음 문장 실행X)
# print('메모장 수행')

import threading, time

def run(id):
    for i in range(1, 21):
        print('id : {} --> {}'.format(id, i))
        
# thread 사용하지 않은 경우
#run(1)
#run(2)

# thread 사용한 경우
th1 = threading.Thread(target=run, args = ('일'))
th1.start()
th2 = threading.Thread(target=run, args = ('이'))
th2.start()
th1.join()
th2.join()

print('작업종료')



