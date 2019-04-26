'''
Server端流程
1.建立socket
2.绑定端口与ip地址   sock.bind()/
3.接受对方文件
4.反馈
'''


import socket
import time

def serverFunc():
    #1.建立socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #2.绑定
    addr = ("127.0.0.1",7852)
    sock.bind(addr)
    #3.接受信息以及地址
    data, addr = sock.recvfrom(500)
    #print(data)
    #print(type(data))

    text = data.decode()       #解码
    print(text)
    #print(type(text))

    #4.反馈
    rsp = "Ich had keine Hunge"

    data = rsp.encode()        #编码
    sock.sendto(data,addr)


if __name__ == '__main__':
    while True:
        print("Start....")
        try:
            serverFunc()
        except Exception as e:
            print(e)
        print("End....\n\n\n")
        time.sleep(1)
