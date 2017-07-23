# thief

标签： tcp 


----------
## Description ##
This is a small tool of tcp, which can tranform terminal command you wana run from your server running server.py to a computer that is running the client.py in this project.


----------
## Usage ##
To run server:
```
    python server.py
```    

cmd | useage | example
--- | ------ | -------
dld filename | show the detail of the file | dld test.txt
exit1997 | disconnect and end operation | exit1997
cd foldername | get into a folder(the same in windows) | cd test
others | the same commands in the operation system runing client.py | ... 

To run client:

 1. remember to change the ip to yours
```
    s.connect(('165.227.9.185', 9999))
```
 2. run it:
```
    python client.py
```
----------

## Rendering ##
![rendering][1]
![rendering show][2]


  [1]: https://github.com/gzm1997/thief/blob/master/screenshots/thief.gif?raw=true
  [2]: https://github.com/gzm1997/thief/blob/master/screenshots/thief.png?raw=true
