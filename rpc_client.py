import socket
import json
def create_socket(message):
    HOST, PORT = "127.0.0.1", 8081

    # Create a socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Connect to the socket
    client.connect((HOST, PORT))

    # Sending message to server
    client.send(message.encode())

    # Receive message from server
    response = client.recv(1024).decode()

    # Close the connection
    client.close()

    return response

def add(a,b,c):
	data = {
		"procedure_name": "add",
		"parameters": [
			{
				"parameter_value": a,
			},
			{
				"parameter_value": b,
			},
			{
				"parameter_value": c,
			}
		]
	}

	message = json.dumps(data)
	response = create_socket(message)

	return response

def mul(a,b):
	data = {
		"procedure_name": "mul",
		"parameters": [
			{
				"parameter_value": a,
			},
			{
				"parameter_value": b,
			}
		]
	}

	message = json.dumps(data)
	response = create_socket(message)

	return response

def foo(a,b):
	data = {
		"procedure_name": "foo",
		"parameters": [
			{
				"parameter_value": a,
			},
			{
				"parameter_value": b,
			}
		]
	}

	message = json.dumps(data)
	response = create_socket(message)

	return response

def bar(a):
	data = {
		"procedure_name": "bar",
		"parameters": [
			{
				"parameter_value": a,
			}
		]
	}

	message = json.dumps(data)
	response = create_socket(message)

	return response

