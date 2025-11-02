import socket

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP socket

print("Socket created successfully!")
s.close()
