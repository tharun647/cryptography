from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

def add_padding(data, block_size):
    padder = padding.PKCS7(block_size * 8).padder()
    return padder.update(data) + padder.finalize()

def remove_padding(padded_data):
    unpadder = padding.PKCS7(128).unpadder()
    return unpadder.update(padded_data) + unpadder.finalize()

def encrypt_decrypt(mode, key, iv, data):
    cipher = Cipher(algorithms.AES(key), mode, backend=default_backend())
    encryptor = cipher.encryptor()
    padded_data = add_padding(data, 16)
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    decryptor = cipher.decryptor()
    decrypted = remove_padding(decryptor.update(ciphertext) + decryptor.finalize())
    return ciphertext, decrypted

def main():
    key = b"this_is_a_16_key"
    iv = b"this_is_a_16_iv_"
    plaintext = b"This is a plaintext message for testing."

    print("Original Data:", plaintext)

    ecb_cipher, ecb_decrypted = encrypt_decrypt(modes.ECB(), key, iv, plaintext)
    print("ECB Ciphertext:", ecb_cipher)
    print("ECB Decrypted:", ecb_decrypted)

    cbc_cipher, cbc_decrypted = encrypt_decrypt(modes.CBC(iv), key, iv, plaintext)
    print("CBC Ciphertext:", cbc_cipher)
    print("CBC Decrypted:", cbc_decrypted)

if __name__ == "__main__":
    main()
Original Data: b'This is a plaintext message for testing.'
ECB Ciphertext: b'\xcamQ\xc1\xe5\x84\xe9\xa1\xbdSa\xa6\xe4l\x8cd\xdd\x7fm\x7f\x80M\x1a\xed3\xa3Q\xd4\xe1\xb1+u\x19\\\xb4k\xb8\xba\x1e\xab`x\x05\xca\x9e7\xa3\xce'
ECB Decrypted: b'This is a plaintext message for testing.'
CBC Ciphertext: b'\x91\xcd\x9a\xf3,=4,DJ\x94?d\x07\xe5\xecc\x93\xf4\x90\x8b\x1b\x02)\xa9\xc1\xff\xc3\xa8\xa0\xe3\xf0.\x7f^\x14a/\xf3\xf3\x8c\x8bMj1\xa5\xc5\x93'
CBC Decrypted: b'This is a plaintext message for testing.'
