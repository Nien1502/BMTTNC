"""
Caesar Cipher Implementation

Công thức mã hóa Caesar:
E = (plaintext + key) % 26  - Encryption
D = (cipher - key) % 26     - Decryption

Ví dụ: 
- A (index=0) + key=3 = D (index=3)
- Z (index=25) + key=3 = C (index=2) vì (25+3)%26 = 2
"""

from .alphabet import ALPHABET

class CaesarCipher:
    def __init__(self):
        self.alphabet = ALPHABET
    
    # E = (plain + key) % 26
    def encrypt(self, plain: str, key: int): #Hutech , key = 5
        plain_text = plain.upper() #Hutech
        len_alp = len(self.alphabet) #26
        encrypted = []
        for i in plain_text: #H
            letters = self.alphabet.index(i) #72
            cipher = (letters + key) % len_alp #77
            cipher_text = self.alphabet[cipher] #M
            encrypted.append(cipher_text) #list[M,]
        return "".join(encrypted)
    
    def decrypt_text(self, cipher: str, key: int): #Hutech , key = 5
        cipher_text = cipher.upper() #Hutech
        len_alp = len(self.alphabet) #26
        decrypted = []
        for i in cipher_text: #H
            letters = self.alphabet.index(i) #72
            cipher = (letters + key) % len_alp #77
            decrypted_text = self.alphabet[cipher] #M
            decrypted.append(decrypted_text) #list[M,]
        return "".join(decrypted)