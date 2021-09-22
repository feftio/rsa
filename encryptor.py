from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

public_key = RSA.import_key(open('public_key.pem').read())
message = input('Put your message: ')

encryptor = PKCS1_OAEP.new(public_key)
encrypted = encryptor.encrypt(message.encode())

file_out = open('message', 'wb')
file_out.write(encrypted)
file_out.close()
