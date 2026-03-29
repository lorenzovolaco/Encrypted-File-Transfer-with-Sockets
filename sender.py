import os
import socket
import struct

from Crypto.Cipher import AES

key = b"qwertyuiopasdfgh"
nonce = b"mnbvcxzclkjhgfds"

cipher = AES.new(key, AES.MODE_EAX, nonce)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#usa TCP, não perde data
client.connect(("localhost", 9998))

file_size = os.path.getsize("file")

with open("file", "rb") as f:
    data = f.read()

encrypted = cipher.encrypt(data)

client.send("file.txt".encode())
client.send(struct.pack('!I', file_size))
client.sendall(encrypted)
client.send(b"<Fim>")

client.close()
