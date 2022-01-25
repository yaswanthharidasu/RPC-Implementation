import socket

HOST, PORT = "127.0.0.1", 8081

# Create a socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind IP and port to the socket
server.bind((HOST, PORT))
server.listen(5)
print("Server listening at port: ", PORT, "...", sep="")

while True:
    try:
        conn, addr = server.accept()
        req = conn.recv(1024).decode()
        print("Message from client:", req)
        # send response
        msg = input("Enter response: ")
        response = msg.encode()
        conn.sendall(response)
        # conn.close()
    except Exception as E:
        print(E)