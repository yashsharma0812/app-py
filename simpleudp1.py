import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('127.0.0.1', 12345))

print("UDP Server is running...")

while True:
    data, addr = server.recvfrom(1024)
    print(f"Received '{data.decode()}' from {addr}")
    server.sendto(b"Hello from UDP Server!", addr)
