from socket import *

clientsock = socket(AF_INET, SOCK_STREAM)
clientsock.connect(('192.168.0.24', 8888))
clientsock.send('안녕!!!!!! scm'.encode(encoding = 'utf-8', errors = 'strict'))
re_msg = clientsock.recv(1024).decode()
print('수신 자료 : ' + re_msg)
clientsock.close()