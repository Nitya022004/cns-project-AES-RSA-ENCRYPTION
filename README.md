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

## **2. Start the Receiver**
In the first terminal, run the receiver:
python receiver/receiver.py

3. Start the Sniffer (Optional)
In the second terminal, simulate an intruder:
bash
Copy code
python intruder/sniffer.py


4. Send a File
In the third terminal, run the sender script and provide the file path to send
python sender/sender.py

5. View the Result
The receiver saves the decrypted file in the received_files/ folder.
Use the sniffer or Wireshark to view the encrypted traffic.

Using Wireshark
1. Select Network Interface
Choose the "Adapter for loopback traffic capture" (if sender and receiver are on the same machine).
2. Apply Filter
Use the filter tcp.port == 65432 to view packets related to file transfer.
3. Analyze TCP Stream
Right-click on a captured packet and choose Follow > TCP Stream to view the encrypted communication.
Conclusion
This project demonstrates practical implementation of AES-RSA encryption for secure file transfer, along with network monitoring using Wireshark.


