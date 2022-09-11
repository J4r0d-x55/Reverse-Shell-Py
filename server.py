from socket import *

ip = "127.0.0.1"
port = 1234

connection = socket(AF_INET, SOCK_STREAM)
connection.bind((ip, port))

connection.listen(1)
client, addr = connection.accept()
print("connect -> "+str(addr))

while True:
    recever = client.recv(1024).decode()
    print(recever)
    cmd = input("entrez votre commande: ")

    if cmd == "exit":
        client.send(cmd.encode())
        exit()
    elif cmd == "" or cmd == None:
        cmd = "erreur"
        client.send(cmd.encode())
    else:
        client.send(cmd.encode())
