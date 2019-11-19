# thread의 활성화 / 비활성화 (wait() / notify())

import threading, time

bread_plate = 0 # 빵접시 -  공유 자원
lock = threading.Condition()

class Maker(threading.Thread): # 빵을 만드는 생산자
    def run(self):
        global bread_plate
        for i in range(30):
            lock.acquire()
            while bread_plate >= 10:
                print('빵 생산 초과로 대기')
                lock.wait() # 스레드 비 활성화
            bread_plate += 1
            print('빵 생산 :',bread_plate)
            lock.notify() # 스레드 활성화
            lock.release()
            time.sleep(0.05)
            
class Consumer(threading.Thread): # 소비자
    def run(self):
        global bread_plate
        for i in range(30):
            lock.acquire()
            while bread_plate< 1:
                print('빵이 없어 기다림.....')
                lock.wait() # 스레드 비 활성화
            bread_plate -= 1
            print('빵 소비 :',bread_plate)
            lock.notify() # 스레드 활성화
            lock.release()
            time.sleep(0.03)
            
mak = []
con = []
for i in range(5): # 생산자 수
    mak.append(Maker())

for i in range(5): # 소비자 수
    con.append(Consumer())
    
for th1 in mak:
    th1.start()

for th2 in con:
    th2.start()
    
for th1 in mak:
    th1.join()

for th2 in con:
    th2.join()