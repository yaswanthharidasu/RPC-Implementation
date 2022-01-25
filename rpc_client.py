import socket

HOST, PORT = "127.0.0.1", 8081

# Create a socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

client.connect((HOST, PORT))

while True:
    # Read message from user
    message = input("Enter message:")
    # Exit condition
    if(message == "exit"):
        break
    # Sending message to server
    client.send(message.encode())
    # Receive message from server
    print("Reply from server:", client.recv(1024).decode())

# Close the connection
client.close()