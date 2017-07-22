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
    sock.send(b"welcome!")
    f = open("t.txt", "wb")
    f.close()

    while True:
        data = sock.recv(1024)
        f = open("t.txt", "ab")
        f.write(data.decode("gb2312").encode("utf-8"))

        time.sleep(1)
        if data.decode("gb2312").find("exit") != -1:
            print("accpet exit")
            break
    sock.close()
    print("connection from %s:%s closed" % addr)


"""
sock, addr = s.accept()
t = threading.Thread(target = tcplink, args = (sock, addr))
t.start()
"""


while True:
    sock, addr = s.accept()
    t = threading.Thread(target = tcplink, args = (sock, addr))
    t.start()

