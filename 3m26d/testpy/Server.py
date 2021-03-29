import socket as sk
import threading
from threading import Lock,Thread


def read_data(sock:sk.socket):
    while True:
        print(id(sock))
        data = sock.recv(9999)
        print("接受信息：",data)

def send_data(sock:sk.socket):
    while True:
        print(id(sock))
        send_msg = input("输入信息：")
        sock.send(bytes(send_msg,encoding="utf-8"))
def main():
    so1 = sk.socket(sk.AF_INET,sk.SOCK_STREAM)
    so1.setsockopt(sk.SOL_SOCKET,sk.SO_REUSEADDR,1) 
    #host = sk.gethostname()
    host = "127.0.0.1"
    port = 8849
    #print("host is : ",host)
    so1.bind((host,port))
    so1.listen(5)
    c,addr = so1.accept()     # 建立客户端连接
    print(id(c))
    print("连接地址：", addr)
    th = threading.Thread(target=read_data,args=(c,))
    th.start()
    send_data(c)

if( __name__ == "__main__"):
    main()