import os
import socket
from decrypt_utils import decrypt_file, decrypt_with_rsa

SERVER_ADDRESS = ('127.0.0.1', 65432)

def receive_all(conn):
    buffer = b''
    while True:
        chunk = conn.recv(4096)
        if not chunk:
            break
        buffer += chunk
    return buffer

def start_receiver(private_key_path):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(SERVER_ADDRESS)
        s.listen()
        print("Waiting for sender...")
        conn, addr = s.accept()
        with conn:
            # Receive and parse data
            data = receive_all(conn)
            filename, encrypted_key, encrypted_file = data.split(b'||', 2)
            
            # Decrypt AES key with RSA
            with open(private_key_path, 'rb') as f:
                private_key = f.read()
            aes_key = decrypt_with_rsa(encrypted_key, private_key)
            
            # Decrypt file
            decrypted_data = decrypt_file(encrypted_file, aes_key)
            
            # Ensure the output directory exists
            output_dir = 'received_files'
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
            
            save_path = os.path.join(output_dir, filename.decode())
            with open(save_path, 'wb') as f:
                f.write(decrypted_data)
            print(f"File received and decrypted! Saved as '{save_path}'.")

if __name__ == '__main__':
    private_key_path = 'keys/private_key.pem'
    start_receiver(private_key_path)
