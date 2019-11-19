# 연결 지향 프로토콜  (TCP/IP)
# socket 모듈 사용 : 컴퓨터 간 인터페이스 가능

import socket

print(socket.getservbyname('http','tcp'))
print(socket.getservbyname('telnet','tcp'))
print(socket.getservbyname('ftp','tcp'))
print(socket.getaddrinfo('www.naver.com', 80, proto = socket.SOL_TCP))
print(socket.getaddrinfo('www.daum.net', 80, proto = socket.SOL_TCP))

