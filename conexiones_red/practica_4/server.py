#!/usr/bin/env python3

import socket

def start_chat_server():
    host = 'localhost'
    port = 1234
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #Time web
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"\n[+] Servidor listo para aceptar una conexión...")
    connetion, clien_addr = server_socket.accept()
    print(f"\n[+] Se ha conectado el cliente: {clien_addr}")
    
    while True:
        client_message = connetion.recv(1024).strip().decode()
        print(f"\n[+] Mensaje del cliente: {client_message}")
        
        if client_message == "bye":
            break
        
        server_message = input(f"\n[+] Mensaje para el cliente: ")
        connetion.send(server_message.encode())
    
    connetion.close()

start_chat_server()