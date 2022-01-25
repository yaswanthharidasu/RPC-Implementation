import json

FILE_NAME = "rpc_server.py"
file = open(FILE_NAME, "w")

def generate_socket():
    socket_code = """HOST, PORT = "127.0.0.1", 8081

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
        
"""

    file.write(socket_code)


def generate_process_request():
    request_code = '''def process_request(req):
\tdata = json.loads(req)
\tparameters = '('

\tfor i in range(len(data["parameters"])):
\t\tparameters += str(data["parameters"][i]["parameter_value"])
\t\tif i != len(data["parameters"])-1:
\t\t\tparameters += ","

\tparameters += ')'
\tfunc_name = data['procedure_name'] + "_stub"

'''

    contract = open('contract.json')
    data = json.load(contract)


    if_code = ""
    if_code += "\tfunc_name += parameters\n\n"
    if_code += "\treturn eval(func_name)\n\n"
    
    file.write(request_code)
    file.write(if_code)



def generate_procedure(procedure):
    header_code = "def "+procedure['procedure_name'] + "_stub("
    body_code = "\t"

    if 'return_type' in procedure and procedure['return_type'] != "None":
        body_code += "return " + procedure['return_type'] + "("

    body_code += "sp."+procedure['procedure_name'] + "("
    parameters = procedure['parameters']
    for i in range(len(parameters)):
        if i >= 1:
            header_code += ","
            body_code += ","
        body_code += parameters[i]['data_type']+ "(" + parameters[i]["parameter_name"] + ")"
        header_code += parameters[i]['parameter_name']

    header_code += "):\n"
    body_code += ")"
    if 'return_type' not in procedure or procedure['return_type'] == "None":
        body_code += "\n\treturn 'No return value'"
    else:
        body_code += ")"
    body_code += "\n\n\n"
    # Send message to server
    file.write(header_code)
    file.write(body_code)


if __name__ == "__main__":

    import_code = """import socket
import json 
import server_procedures as sp

"""
    file.write(import_code)

    # Write all the func_codetions, which are in the contract.json file
    contract = open('contract.json')
    data = json.load(contract)

    for procedure in data['remote_procedures']:
        generate_procedure(procedure)

    generate_process_request()
    # Generate socket func_codetionality
    generate_socket()
