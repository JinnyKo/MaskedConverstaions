from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64
import hashlib
from Crypto import Random

class AESCipher:
    def __init__(self, key):
        self.key = hashlib.sha256(key.encode()).digest()
        self.bs = 16

    def encrypt(self, raw):
        raw = pad(raw.encode(), self.bs)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        encrypted = base64.b64encode(iv + cipher.encrypt(raw))
        return encrypted.decode('utf-8')

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        decrypted = unpad(cipher.decrypt(enc[AES.block_size:]), self.bs)
        return decrypted.decode('utf-8')
