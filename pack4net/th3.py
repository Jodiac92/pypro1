# 스레드 클래스 상속

import threading, time, sys

"""
class MyClass(threading.Thread):
    def run(self):
        for i in range(1, 11):
            print('id : {} => {}'.format(self.getName(), i))
            time.sleep(0.5)


ths = []
for i in range(2):
    th = MyClass()
    th.start()
    ths.append(th)

for t in ths:
    t.join()
"""

class MyClock(threading.Thread):
    def run(self):
        while 1:
            now = time.localtime()
            if 9 <= now.tm_hour < 14:
                print('오전 근무 및 점심 시간')
            elif 14 <= now.tm_hour < 18:
                print('오후 근무 시간')
            else:
                print('자유 시간')
                sys.exit()
            print('현재는 {}년 {}월 {}일 {}시 {}분 {}초'.format(now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec))
            time.sleep(1)
            
work = MyClock()
work.start()
work.join()
print('종료')