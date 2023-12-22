import socket
from utils import ANSWERS


server_host = '127.0.0.1'
server_port = 8001

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_host, server_port))
server_socket.listen(1)
print(f"Server listening on {server_host}:{server_port}")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address}")

    data = client_socket.recv(1024).decode('utf-8')
    print("Data in server:", data)

    # Assuming your translation function is defined in 'utils'

    try:
        answer = ANSWERS.get(data)
    except:
        answer = 'answer not found!!!'

    try:
        answer = ANSWERS.get(data)
        if answer is None:
            answer = 'answer not found!!!'
    except Exception as e:
        print(f"Error getting answer: {e}")
        answer = 'error getting answer'

    client_socket.send(answer.encode('utf-8'))
    client_socket.close()
