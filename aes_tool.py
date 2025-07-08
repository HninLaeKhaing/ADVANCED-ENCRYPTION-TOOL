
from Cryptodome.Cipher import AES
from Cryptodome.Hash import SHA256
from Cryptodome import Random
import os

def get_key(password):
    return SHA256.new(password.encode('utf-8')).digest()

def encrypt_file(file_path, password):
    key = get_key(password)
    chunk_size = 64 * 1024
    output_file = file_path + ".enc"
    iv = Random.new().read(16)
    encryptor = AES.new(key, AES.MODE_CBC, iv)

    with open(file_path, 'rb') as infile, open(output_file, 'wb') as outfile:
        outfile.write(iv)
        while True:
            chunk = infile.read(chunk_size)
            if len(chunk) == 0:
                break
            elif len(chunk) % 16 != 0:
                chunk += b' ' * (16 - len(chunk) % 16)
            outfile.write(encryptor.encrypt(chunk))

    print(f"[+] File encrypted successfully: {output_file}")

def decrypt_file(file_path, password):
    key = get_key(password)
    chunk_size = 64 * 1024
    output_file = file_path.replace(".enc", ".dec")

    with open(file_path, 'rb') as infile, open(output_file, 'wb') as outfile:
        iv = infile.read(16)
        decryptor = AES.new(key, AES.MODE_CBC, iv)

        while True:
            chunk = infile.read(chunk_size)
            if len(chunk) == 0:
                break
            outfile.write(decryptor.decrypt(chunk))

    print(f"[+] File decrypted successfully: {output_file}")

# Example usage (edit and run manually)
# encrypt_file("example.txt", "mypassword")
# decrypt_file("example.txt.enc", "mypassword")
