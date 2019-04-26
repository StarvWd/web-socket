'''
1.建立通信的socket
2.链接对方，请求建立通路
3.发送
4.接收
5.关闭链接通路
'''

import socket


def tcp_clt():
    #1.建立socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #2.链接请求
    addr = ("127.0.0.1", 8888)
    sock.connect(addr)
    #3.发送
    msg = "My Infromation"
    sock.send(msg.encode())
    #4.接收
    rst = sock.recv(500)
    print(rst.decode())
    #5.关闭
    sock.close()



if __name__ == '__main__':
    tcp_clt()
