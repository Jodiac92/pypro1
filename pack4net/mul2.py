# 병렬 처리를 위한 process

import os
from multiprocessing import Process

def func():
    print('연속적으로 진행하고자 하는 작업')
    
def doubler(number):
    result = number + 10
    func()
    pid = os.getpid()
    print('number : {}, result : {}, pid : {}'.format(number, result, pid))
    
if __name__ == '__main__':
    numbers = [1,2,3,4,5]
    procs = []
    
    for idx, number in enumerate(numbers):
        proc = Process(target = doubler, args = (number,))
        procs.append(proc)
        proc.start()
        
    for proc in procs:
        proc.join()