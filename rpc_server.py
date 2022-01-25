import socket
import json 
import server_procedures as sp

def add_stub(a,b,c):
	return int(sp.add(int(a),int(b),float(c)))


def mul_stub(a,b):
	return int(sp.mul(int(a),int(b)))


def foo_stub(a,b):
	sp.foo(int(a),int(b))
	return 'No return value'


def bar_stub(a):
	sp.bar(str(a))
	return 'No return value'


def process_request(req):
	data = json.loads(req)
	parameters = '('

	for i in range(len(data["parameters"])):
		parameters += str(data["parameters"][i]["parameter_value"])
		if i != len(data["parameters"])-1:
			parameters += ","

	parameters += ')'
	func_name = data['procedure_name'] + "_stub"

	func_name += parameters

	return eval(func_name)

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
        # send response
        msg = str(process_request(req))
        response = msg.encode()
        conn.sendall(response)
        # conn.close()
    except Exception as E:
        print(E)
        
