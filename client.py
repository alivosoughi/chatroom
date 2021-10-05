import socket 
import sys 
  
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
if len(sys.argv) != 3: 
    print("Correct usage: script, IP address, port number")
    exit() 
IP_address = str(sys.argv[1]) 
Port = int(sys.argv[2]) 
server.connect((IP_address, Port))
name = input("enter your name:\n")
server.sendall(name.encode('utf-8'))
  
while True: 
  
    instrc = int(input("1.List  2.Send\n3.Recieve   4.Exit\n"))

    if instrc == 1:
        server.sendall(b"List")
        List = server.recv(1024)
        print("name of clients:\n")
        print(List.decode('utf-8'))
    elif instrc == 2:
        server.sendall(b"Send")
        recvName = input("enter reciever name:\n")
        message = input("type your message:\n")
        server.sendall(recvName.encode('utf-8'))
        if server.recv(2048) == b"sendmsg":
        	server.sendall(message.encode('utf-8'))
        else:
        	print("some error occured\n")
    elif instrc == 3:
        recv_message = server.recv(1024)
        print(recv_message.decode('utf-8'))
    elif instrc == 4:
        break;
    else:
        print("invalid input\n")

server.close() 