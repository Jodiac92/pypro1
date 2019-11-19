import socket
import threading

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.bind(('192.168.0.24', 5555))
ss.listen(5)
print('채팅 서버 서비스 시작...')

users = []

def ChatUser(conn):
    name = conn.recv(1024)
    data = '^^ ' + name.decode('utf-8') + '님 입장 ^^'
    print(data)
    
    try:
        for p in users:
            p.send(data.encode('utf-8'))
            
        while True:
            msg = conn.recv(1024)
            data = name.decode('utf-8') + '님 메시지 : ' + msg.decode('utf-8')
            print('수신 : ' + data)
            for p in users:
                p.send(data.encode('utf-8'))
    except:
        users.remove(conn)
        data = name.decode('utf-8') + '님 퇴장'
        print(data)
        if users:
            for p in users:
                p.send(data.encode('utf-8'))
        else:
            print('exit')
while True:
    conn, addr = ss.accept()
    users.append(conn)
    th = threading.Thread(target=ChatUser, args = (conn,))
    th.start()
    