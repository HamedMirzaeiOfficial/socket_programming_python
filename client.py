import socket

client_host = '127.0.0.1'
client_port = 8003
interface_address = ('127.0.0.1', 8002)

interface_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    message = input("Enter a word: ")

    interface_socket.sendto(message.encode('utf-8'), interface_address)

    translated_data, _ = interface_socket.recvfrom(1024)
    print(f"message: {translated_data.decode('utf-8')}")
