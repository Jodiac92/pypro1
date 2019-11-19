# echo server 서비스 계속 유지

import socket
import sys

HOST = ''
PORT = 8888


serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    serversock.bind((HOST, PORT))
    print('에코 서버 서비스 시작')
    serversock.listen(5)
    
    while 1:
        conn, addr = serversock.accept()
        print('접속자 컴의 정보 : ', addr[0], addr[1])
        print(conn.recv(1024).decode()) # 수신 메시지 출력
        
        # 메시지 전송
        conn.send(('from server : ' + '잘 살어라').encode('utf-8'))
        
except socket.error as err:
    print('에러 : ',err)
    sys.exit()
finally:
    serversock.close()
    conn.close()