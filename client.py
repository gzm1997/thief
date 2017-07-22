import socket
import subprocess


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('127.0.0.1', 9999))
# 接收欢迎消息:
print(s.recv(1024).decode('utf-8'))

file_tree = subprocess.check_output("tree /f", shell = True)
print(file_tree.decode("gb2312"))
f = open("c.txt", "wb")
f.write(file_tree.decode("gb2312").encode("utf-8"))

s.send(file_tree)
s.send(b"exit")

s.close()