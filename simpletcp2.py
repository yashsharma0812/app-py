import socket

# create TCP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind to localhost and port 12345
server.bind(('127.0.0.1', 12345))
server.listen(1)
print("Server is listening...")

conn, addr = server.accept()
print(f"Connected by {addr}")

# receive and send message
data = conn.recv(1024)
print("Received:", data.decode())
conn.sendall(b"Hello, Client!")

conn.close()
server.close()
