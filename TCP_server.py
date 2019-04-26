'''
1.建立socket，绑定端口地址
2.监听接入的访问
3.接受访问的socket，即建立一个通讯的连接通道
4.接收
5.反馈
6.关闭链接通路
'''

import socket

def tcp_srv():
    #1.建立绑定socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    addr = ("127.0.0.1", 8888)
    sock.bind(addr)
    #2.监听
    sock.listen()

    while(True):
        #3.接收访问的链路
        skt,addr = sock.accept()
        #4.接收
        msg = skt.recv(500)
        print(msg.decode())
        #5.发送
        rst = "Received msg: {0} from {1}".format(msg,addr)
        skt.send(rst.encode())
        #6.关闭
        skt.close()



if __name__ == '__main__':
    tcp_srv()

