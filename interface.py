import socket
from utils import translator

interface_host = '127.0.0.1'
interface_port = 8002
server_address = ('127.0.0.1', 8001)

interface_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
interface_socket.bind((interface_host, interface_port))
print(f"Interface listening on {interface_host}:{interface_port}")

while True:
    try:
        data, client_address = interface_socket.recvfrom(1024)
        print(f"Received from client: {data.decode('utf-8')}")

        # Translating data from Persian to English
        translated_data = translator(data.decode('utf-8'))
        print(f"message: {translated_data}")
        

        # Creating a TCP socket for communication with the server
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.connect(server_address)

        # Sending translated data to the server
        server_socket.send(translated_data.encode('utf-8'))

        # Receiving response from the server
        data_from_server = server_socket.recv(1024).decode('utf-8')
        print(f"Received from server: {data_from_server}")

        translated_to_persian = translator(data_from_server)
        print(f"Received from server translated: {translated_to_persian}")

        # Sending translated response back to the client
        interface_socket.sendto(translated_to_persian.encode('utf-8'), client_address)

        # Close the server socket
        server_socket.close()

    except Exception as e:
        print(f"Error: {e}")
        # Handle the error as needed
