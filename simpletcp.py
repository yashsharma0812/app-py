import socket

# create TCP socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to server (localhost, port 12345)
client.connect(('127.0.0.1', 12345))
print("Connected to server!")

# send message
client.sendall(b"Hello, Server!")
data = client.recv(1024)
print("Received from server:", data.decode())

client.close()
