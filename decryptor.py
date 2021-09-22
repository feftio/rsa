from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

private_key = RSA.import_key(open('private_key.pem').read())

cipher_rsa = PKCS1_OAEP.new(private_key)
decrypted = cipher_rsa.decrypt(open('message', 'rb').read())

print('Decrypted message:', decrypted.decode())
input()
