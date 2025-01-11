from Crypto.PublicKey import RSA

def generate_keys():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    with open("keys/private_key.pem", "wb") as priv_file:
        priv_file.write(private_key)
    with open("keys/public_key.pem", "wb") as pub_file:
        pub_file.write(public_key)

if __name__ == "__main__":
    generate_keys()
