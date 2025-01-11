import os
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Util.Padding import pad

def generate_aes_key():
    return os.urandom(16)

def encrypt_file(file_path, aes_key):
    with open(file_path, 'rb') as f:
        data = f.read()
    cipher = AES.new(aes_key, AES.MODE_CBC)
    iv = cipher.iv
    encrypted_data = cipher.encrypt(pad(data, AES.block_size))
    return iv + encrypted_data

def encrypt_with_rsa(data, public_key):
    rsa_key = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(rsa_key)
    return cipher.encrypt(data)
