from socket import *

serversock = socket(AF_INET, SOCK_STREAM) # 소켓 종류, 소켓 유형
serversock.bind(('192.168.0.24', 9999))
serversock.listen(1) # 동시 접속자 수
print('서비스 시작....')

conn, addr = serversock.accept()
print('conn : ', conn)
print('addr : ', addr)
print('from client message : ', conn.recv(1024).decode())
conn.close()
serversock.close()