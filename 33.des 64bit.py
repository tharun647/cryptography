from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

def pkcs7_padding(data):
    """Applies PKCS#7 padding."""
    pad_byte = 8 - (len(data) % 8)
    return data + bytes([pad_byte] * pad_byte)

def pkcs7_unpadding(data):
    """Removes PKCS#7 padding."""
    return data[:-data[-1]]

def des_encrypt(plain_text, key):
    """Encrypts given plain_text using DES and the given key."""
    padded_text = pkcs7_padding(plain_text)
    cipher = DES.new(key, DES.MODE_ECB)
    return cipher.encrypt(padded_text)

def des_decrypt(ciphertext, key):
    """Decrypts given ciphertext using DES and the given key."""
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted = cipher.decrypt(ciphertext)
    return pkcs7_unpadding(decrypted)

# Key should be 64 bits, which is 8 bytes, but only 56 bits are used for encryption (the rest are parity bits).
key = get_random_bytes(8)
print(f"Key: {key.hex()}")

# Plain text can be of variable length; padding will make it a multiple of 8 bytes
plain_text = b"Hello, DES!"
print(f"Plain text: {plain_text}")

# Encrypt the plain text
encrypted_text = des_encrypt(plain_text, key)
print(f"Encrypted text: {encrypted_text.hex()}")

# Decrypt the encrypted text
decrypted_text = des_decrypt(encrypted_text, key)
print(f"Decrypted text: {decrypted_text.decode()}")

Key: 07b1a24ddcd1a835
Plain text: b'Hello, DES!'
Encrypted text: a39733583a465a863670073b84b1bbbc
Decrypted text: Hello, DES!
