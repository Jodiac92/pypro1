# python에서 thread는 GIL 정책을 따르므로 그로 인해 진정한 병렬 불가
# multi processing을 위한 Pool, Process API를 이용하여 이것을 해결!

# Pool 사용 예
from multiprocessing import Pool
import time
import os

def func(x):
    print('값 ', x, '에 대한 작업 process pid :', os.getpid())
    time.sleep(1)
    return x * x

if __name__ == '__main__':
    p = Pool(4) # 3 ~ 5개가 적당
    startTime = int(time.time())
    
    # for i in range(0, 10):
    #     print(func(i))
    
    print(p.map(func, range(0, 10)))    
    endTime = int(time.time())
    print('총 작업시간 :',endTime - startTime)
