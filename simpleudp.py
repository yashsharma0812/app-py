import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.sendto(b"Hello, UDP Server!", ('127.0.0.1', 12345))
data, addr = client.recvfrom(1024)
print("Received from server:", data.decode())

client.close()
