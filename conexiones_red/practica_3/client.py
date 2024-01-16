import socket

def start_client():
    host = 'localhost'
    port = 1234
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        
        while True:
            message = input(f"\n[+] Introduce tu mensaje: ")
            s.sendall(message.encode())
            
            if message == "bye":
                break
            
            data = s.recv(1024)
            print(f"\n[+] Mensaje de respuesta del servidor: {data.decode()}")
            
start_client()