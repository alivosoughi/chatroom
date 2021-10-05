import socket 
import sys 
from _thread import *
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
if len(sys.argv) != 3: 
    print("Correct usage: script, IP address, port number")
    exit() 
IP_address = str(sys.argv[1]) 
Port = int(sys.argv[2]) 
server.bind((IP_address, Port)) 
server.listen(100) 
  
list_of_clients = [] 
name_of_clients = []


def print_list(list):
    element_str = ""
    for i in list:
        element_str = element_str + i.decode('utf-8') + "\n"

    return element_str

def find_conn(recv_name):
    return list_of_clients[name_of_clients.index(recv_name)]
  
def clientthread(conn, addr, name): 
    while True: 
        inst = conn.recv(2048)
        if inst == b"List":
            name_str = print_list(name_of_clients)
            try:
                conn.sendall(name_str.encode('utf-8'))
            except:
                conn.close() 
                remove(conn, name) 
        elif inst == b"Send":
            recv_name = conn.recv(2048)
            conn.sendall(b"sendmsg")
            recv_message = conn.recv(2048)
            recv_conn = find_conn(recv_name)
            send_message = "< " + name.decode('utf-8') + " >" + " " + recv_message.decode('utf-8') + "\n"
            try:
                recv_conn.sendall(send_message.encode('utf-8'))
            except: 
                recv_conn.close() 
                remove(recv_conn, recv_name) 
           
def remove(connection, name): 
    if connection in list_of_clients: 
        list_of_clients.remove(connection)
        name_of_clients.remove(name)
  
while True: 
    conn, addr = server.accept() 
    name = conn.recv(2048)
    list_of_clients.append(conn) 
    name_of_clients.append(name)
    print(addr[0] + " connected")
    start_new_thread(clientthread,(conn,addr,name))     
  
conn.close() 
server.close() 