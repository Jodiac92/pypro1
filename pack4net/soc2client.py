from socket import *

clientsock = socket(AF_INET, SOCK_STREAM)
clientsock.connect(('192.168.0.80', 9999))
clientsock.send('안녕!!!!!! scm'.encode(encoding = 'utf-8', errors = 'strict'))
clientsock.close()