import socket as sk
from Server import *
client = sk.socket(sk.AF_INET,sk.SOCK_STREAM)
print(id(client))
host = "127.0.0.1"
port = 8849
client.connect((host,port))
th = threading.Thread(target=read_data,args=(client,))
th.start()
send_data(client)
