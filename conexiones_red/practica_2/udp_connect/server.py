#!/usr/bin/env python3

import socket

def start_udp_server():
    
    host = 'localhost'
    port = 1234
    # Conexiones UDP
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((host, port))
        print(f"\n[+] Servidor UDP iniciado en: {host}:{port}")
        
        while True:
            data, addr = s.recvfrom(1024)
            print(f"\n[+] Mensaje enviado por el cliente: {data.decode()}")
            print(f"\n[+] Información del cliente que nos ha enviado el mensaje: {addr}")

start_udp_server()