import os
import socket
from encrypt_utils import encrypt_file, generate_aes_key, encrypt_with_rsa

SERVER_ADDRESS = ('127.0.0.1', 65432)

def send_file(file_path, public_key_path):
    # Generate AES key
    aes_key = generate_aes_key()

    # Encrypt the file with AES
    encrypted_file = encrypt_file(file_path, aes_key)
    
    # Encrypt AES key with RSA
    with open(public_key_path, 'rb') as f:
        public_key = f.read()
    encrypted_aes_key = encrypt_with_rsa(aes_key, public_key)
    
    # Send file and encrypted key
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(SERVER_ADDRESS)
        # Send filename, encrypted AES key, and encrypted file data
        filename = os.path.basename(file_path)
        s.sendall(filename.encode() + b'||' + encrypted_aes_key + b'||' + encrypted_file)
    print(f"File '{file_path}' sent successfully!")

if __name__ == '__main__':
    file_path = input("Enter the path of the file to send: ").strip().strip('"')
    public_key_path = 'keys/public_key.pem'

    send_file(file_path, public_key_path)
