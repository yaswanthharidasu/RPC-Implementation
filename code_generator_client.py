import json

FILE_NAME = "rpc_client.py"
file = open(FILE_NAME, "w")

procedure_names = {
    "add": '"add"',
    "mul": '"mul"',
    "foo": '"foo"',
    "bar": '"bar"'
}

def generate_socket():
    socket_code = """import socket
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

"""
    file.write(socket_code)


def generate_procedure(procedure):
    func_code = "def "+procedure['procedure_name'] + "("
    data = '\tdata = {\n\t\t"procedure_name": ' + procedure_names[procedure['procedure_name']] +","
    data += '\n\t\t"parameters": [\n'
    parameters = procedure['parameters']
    for i in range(len(parameters)):
        if i >= 1:
            func_code += ","
            data += ",\n"
        data += '\t\t\t{\n\t\t\t\t"parameter_value": ' + \
            parameters[i]['parameter_name'] + ",\n" + "\t\t\t}"
        func_code += parameters[i]['parameter_name']

    func_code += "):\n"
    data += '\n\t\t]\n\t}\n\n'

    json_code = "\tmessage = json.dumps(data)\n"
    socket_code = "\tresponse = create_socket(message)\n\n"
    return_code = "\treturn response\n\n"

    # Send message to server
    file.write(func_code)
    file.write(data)
    file.write(json_code)
    file.write(socket_code)
    file.write(return_code)

if __name__ == "__main__":

    # Generate socket func_codetionality
    generate_socket()

    # Write all the func_codetions, which are in the contract.json file
    contract = open('contract.json')
    data = json.load(contract)

    for procedure in data['remote_procedures']:
        generate_procedure(procedure)
