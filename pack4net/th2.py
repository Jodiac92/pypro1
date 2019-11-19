# thread를 이용해 날짜 및 시간 출력

import time

now = time.localtime()
print('현재는 {}년 {}월 {}일 {}시 {}분 {}초'.format(now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec))
 
print('요일은 %d'%(now.tm_wday))
print('오늘은  몇 일차  %d'%(now.tm_yday))

print('----------------------------------------')

import threading

def timeShow():
    now = time.localtime()
    print('현재는 {}년 {}월 {}일 {}시 {}분 {}초'.format(now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec))
    
def myRun():
    while 1:
        now2 = time.localtime()
        if now2.tm_sec == 32: break
        timeShow()
        time.sleep(1)

th = threading.Thread(target=myRun)
th.start()

th.join()
print('프로그램 종료')