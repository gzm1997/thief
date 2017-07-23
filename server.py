import socket
import threading
import time

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
            if len(data) < 1024:
                break
        print(result.decode("gb2312"))
            

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


    