from Crypto.Cipher import AES

key = b"qwertyuiopasdfgh" #precisa ter 16 bytes.
nonce = b"mnbvcxzclkjhgfds"

cipher = AES.new(key, AES.MODE_EAX, nonce)
ciphertext, tag = cipher.encrypt_and_digest(b"Hello World")

print(ciphertext)

cipher = AES.new(key, AES.MODE_EAX, nonce)
print(cipher.decrypt(ciphertext))



