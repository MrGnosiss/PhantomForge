# modules/encryptor.py

from cryptography.fernet import Fernet
import base64

def encrypt_fernet(code, key_b64):
    key = key_b64.encode()
    fernet = Fernet(key)
    encrypted = fernet.encrypt(code.encode())
    return f"""
from cryptography.fernet import Fernet
exec(Fernet(b"{key_b64}").decrypt({encrypted!r}))
"""
