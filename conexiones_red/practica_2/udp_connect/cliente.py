#!/usr/bin/env python3
import socket

def start_udp_client():
    
    host = 'localhost'
    port = 1234
    
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.sendto(b"Hola, aqui estamos tensandola", (host, port))

start_udp_client()

