# CNS Project - AES-RSA Encryption

This project demonstrates a secure file transfer mechanism using **AES encryption** for the file data and **RSA encryption** for the AES key. The project also includes a packet-sniffing simulation and guidance for monitoring network traffic using Wireshark.

---

## **Project Features**
1. **File Encryption and Decryption**:
   - **AES Encryption**: Secures file content.
   - **RSA Encryption**: Secures the AES encryption key.
   - End-to-end security ensures only the intended recipient can decrypt the file.

2. **Packet Sniffer**:
   - A script simulates an intruder sniffing network traffic during file transfer.

3. **Wireshark Integration**:
   - View encrypted traffic using Wireshark for network monitoring and analysis.

---

## **Folder Structure**
- **`intruder/`**:
  - Contains `sniffer.py`, a script to capture packets from the specified port.
- **`keys/`**:
  - Contains the RSA key pair: `private_key.pem` (receiver) and `public_key.pem` (sender).
- **`received_files/`**:
  - Decrypted files are saved here by the receiver.
- **`receiver/`**:
  - `receiver.py`: Handles file decryption and saving.
  - `decrypt_utils.py`: Contains decryption logic for RSA and AES.
- **`sender/`**:
  - `sender.py`: Encrypts and sends files.
  - `encrypt_utils.py`: Handles file encryption.
- **`generate_keys.py`**:
  - Generates the RSA public and private keys.

---

## **How to Use**
### **1. Generate RSA Keys**
Run the `generate_keys.py` script to generate `private_key.pem` and `public_key.pem`:
```bash
python generate_keys.py
