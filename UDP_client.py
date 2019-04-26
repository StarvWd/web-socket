'''
Client端流程
1.建立socket       socket.socket()
2.发送信息          sock.sendto()
3.接受反馈          sock.recvfrom()
'''

import socket

def clientFunc():
    #1.建立socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #2.发送消息
    text = "My Information"
    data = text.encode()

    sock.sendto(data,("127.0.0.1",7852))
    #3.接受反馈
    data,addr = sock.recvfrom(200)

    text = data.decode()
    print(text)


if __name__ == '__main__':
        clientFunc()
