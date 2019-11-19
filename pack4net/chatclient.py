import socket
import threading
import sys

def Handle(socket):
    while True:
        data = socket.recv(1024)
        if not data: continue
        print(data.decode('utf-8'))
        
sys.stdout.flush() # 현재 버퍼 자료를  출력장치로 보내고 버퍼 비우기

name = input('채팅 id 입력 : ')
cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cs.connect(('192.168.0.52', 5555))

cs.send(name.encode('utf-8'))

th = threading.Thread(target=Handle, args = (cs,))
th.start()

while True:
    msg = input('> ') # 채팅메시지
    sys.stdout.flush()
    if not msg:
        continue
    
    cs.send(msg.encode('utf-8'))
    
cs.close()