# 🔐 AES-256 File Encryption and Decryption Tool

A Python-based command-line utility to securely **encrypt** and **decrypt files** using the AES-256 encryption standard (CBC mode). The script uses `pycryptodome` for cryptographic operations.

---

## 👨‍💻 Author

- **Name**: Hnin Lae Khaing  
- **GitHub**: [github.com/hninlaekhaing](https://github.com/hninlaekhaing)  
- **Project**: Built for the CodTech Cybersecurity Internship

---

## 🧩 Features

- 🔑 Password-based AES-256 encryption using SHA-256 key derivation.
- 🛡️ Secure CBC mode with random IV generation.
- 📁 Encrypts and decrypts any file format (text, PDF, images, etc.).
- 🧠 Simple and readable logic, easy to integrate into GUI or larger projects.

---

## 📂 File Structure

aes-file-tool/
├── aes_tool.py # Main encryption/decryption logic
├── README.md # Project documentation

yaml
Copy
Edit

---

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/aes-file-tool.git
   cd aes-file-tool
Install required dependency:

bash
Copy
Edit
pip install pycryptodome
## 🔧 Usage
1. Encrypt a file
python
Copy
Edit
from aes_tool import encrypt_file
encrypt_file("example.txt", "mypassword")
This will generate an encrypted file named:

Copy
Edit
example.txt.enc
2. Decrypt the file
python
Copy
Edit
from aes_tool import decrypt_file
decrypt_file("example.txt.enc", "mypassword")
This will output:

pgsql
Copy
Edit
example.txt.dec
## 🧪 Example
python
Copy
Edit
# Encrypt the file
encrypt_file("confidential.pdf", "secure123")

# Decrypt the file
decrypt_file("confidential.pdf.enc", "secure123")
## ⚠️ Notes
Padding is done with spaces (b' ') if the last chunk is not a multiple of 16 bytes.

Make sure the password used for decryption matches exactly with the encryption password.

This is a basic implementation and not recommended for highly secure production systems without improvements like authenticated encryption (e.g., AES-GCM).

