# 스레드 간 공유 자원, 충동 방지 : lock

import threading, time

g_count = 0 # 전역 변수는 자동으로 스레드의 공유 자원이 됨

lock = threading.Lock()

def threadCount(id, count):
    global g_count
    for i in range(count):
        lock.acquire() # 스레드 간 공유 자원 사용 중 경쟁에 의한 공유 자원 충돌 발생을 방지 위함
        print('id : %s => count : %s, gcount : %s'%(id, count, g_count))
        g_count += 1
        lock.release() # 점유 해제
        time.sleep(0.1)
for i in range(1,6):
    threading.Thread(target=threadCount, args = (i, 5)).start()

time.sleep(1)
print('final g_count : ',g_count)
print('finish')