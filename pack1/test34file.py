# 동이름으로 우편 번호 및 주소 출력

try:
    dong = input('동이름 입력 : ')
#     print(dong)
    
    with open('zipcode.txt', mode = 'r', encoding = 'euc-kr') as f:
        #print(f.readline())
        line = f.readline()
        while line:
            #lines = line.split('\t')
            lines = line.split(chr(9))
            #print(lines) # ['363-823', '충북', '청원군', '현도면 상삼리', '', '52133\n']
            if lines[3].startswith(dong):
                #print(lines)
                print('[' + lines[0] + ']' + lines[1] + ' ' + lines[2] + ' ' + lines[3] + ' ' + lines[4])
            line = f.readline()
except Exception as e:
    print('err :', e)