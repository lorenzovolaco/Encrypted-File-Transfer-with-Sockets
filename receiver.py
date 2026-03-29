import socket
import tqdm #barra de progresso
import struct
from Crypto.Cipher import AES

key = b"qwertyuiopasdfgh"  #reutiliza as seguintes 3 linhas.
nonce = b"mnbvcxzclkjhgfds"

cipher = AES.new(key, AES.MODE_EAX, nonce)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(("localhost", 9998))
server.listen()

while True:
    #aceita e recebe apenas uma transferencia, não utilizei uma condição.

    client, address = server.accept() #address é do IP

    file_name = client.recv(1024).decode()
    print("Recebi nome:", file_name)
    file_size_bytes = client.recv(4)
    file_size = struct.unpack('!I', file_size_bytes)[0]
    print("Recebi tamanho:", file_size)

    file = open(file_name, "wb")

    done = False

    file_bytes = b""

    progress = tqdm.tqdm(unit="B", unit_scale=True, unit_divisor=1000, total=int(file_size))

    while not done:
        data = client.recv(1024)
        if not data:
            break
        file_bytes += data
        if file_bytes[-5:] == b"<Fim>":
            file_bytes = file_bytes[:-5] 
            progress.update(len(file_bytes) - 5)
            break
        else:
            progress.update(len(data))

    print(file_bytes)
    file.write(cipher.decrypt(file_bytes))

    file.close()
    client.close()
    print("Arquivo recebido com sucesso!")

server.close()
