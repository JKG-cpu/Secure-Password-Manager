from cryptography.fernet import Fernet

def load_key(path="vault.key"):
    with open(path, "rb") as key_file:
        return key_file.read()

def encrypt(key, data):
    fernet = Fernet(key)
    if not isinstance(data, bytes):
        data = data.encode()

    cryption = fernet.encrypt(data)
    return cryption

def decrypt(key, data):
    fernet = Fernet(key)

    decryption = fernet.decrypt(data).decode()

    return decryption

if __name__ == "__main__":
    key = load_key()

    password = encrypt(key, "Hello World")
    print(password)
    password = decrypt(key, password)
    print(password)