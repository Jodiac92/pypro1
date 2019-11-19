# main 모듈이 아닌 참조 대상 모듈을 위해 별도 패키지에 작성
tot = 100

def myfunc(arg):
    print(arg)
    print('myfunc 처리 완료')
    if __name__ == '__main__':
        print('최상위 모듈')
#myfunc(1)

def kbs():
    print('대한민국 대표방송')
    
def mbc():
    print('문화방송')