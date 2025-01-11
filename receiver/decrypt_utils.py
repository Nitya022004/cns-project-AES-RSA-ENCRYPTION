from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Util.Padding import unpad
from Crypto.PublicKey import RSA

def decrypt_file(encrypted_data, aes_key):
    iv = encrypted_data[:16]
    cipher = AES.new(aes_key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(encrypted_data[16:]), AES.block_size)

def decrypt_with_rsa(encrypted_data, private_key):
    rsa_key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(rsa_key)
    return cipher.decrypt(encrypted_data)
