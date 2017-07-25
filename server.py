import socket
import threading
import time
from PIL import Image
import io

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(("0.0.0.0", 9999))
s.listen(5)
print("waitting for connection...")

def tcplink(sock, addr):
    print("sock", sock)
    print("addr", addr)
    print("accept from %s:%s" % addr) 
    sock.send(b"you connect successfully!")

    while True:
        to_do = input("input what to run: ")
        sock.send(to_do.encode("utf-8"))
        if to_do == "exit1997":
            break
        result = b""
        while True:
            data = sock.recv(1024)
            result = result + data
            if data.decode("gb2312", "ignore").find("done1997") != -1:
                break
        if to_do.find("dld") != -1 and (to_do.find(".jpg") != -1 or to_do.find(".jpeg") != -1 or to_do.find(".png") != -1 or to_do.find(".gif") != -1 or to_do.find(".tif") != -1):
            i = Image.open(io.BytesIO(bytearray(result[:-9])))
            i.show()
        else:
            print(result.decode("gb2312", "ignore"))
            

        time.sleep(1)
        
    sock.close()
    print("connection from %s:%s closed" % addr)



sock, addr = s.accept()
tcplink(sock, addr)


"""
while True:
    sock, addr = s.accept()
    t = threading.Thread(target = tcplink, args = (sock, addr))
    t.start()
"""


    