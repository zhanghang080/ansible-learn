import socket as sk
import select
serversocket = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
dict1 = {serversocket.fileno(): serversocket, 666:"hello"}
so1 = sk.socket(sk.AF_INET,sk.SOCK_STREAM)
#host = sk.gethostname()
host = "127.0.0.1"
port = 8848
#print("host is : ",host)
so1.bind((host,port))
so1.listen(5)
while True:
    c,addr = so1.accept()     # 建立客户端连接
    print("连接地址：", addr)
    recvData = c.recv(9999)
    print(recvData)
    with open("/Users/shjin/Desktop/mytest/ansible-learn/3m26d/testpy/test.html") as fl:
        send_str = fl.read()
        send_info = bytes(send_str,encoding="utf-8")
        c.send(b'HTTP/1.1 200 OK\r\nContent-Type:text/html;charset=utf-8\r\n\r\n')
        c.send(send_info)
    c.close()
    
    
    