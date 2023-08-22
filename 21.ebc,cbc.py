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
    ciphertext = encryptor.update(add_padding(data, 16)) + encryptor.finalize()
    decryptor = cipher.decryptor()
    decrypted = remove_padding(decryptor.update(ciphertext) + decryptor.finalize())
    return ciphertext, decrypted

def main():
    key = b"this_is_a_16_key"
    iv = b"this_is_a_16_iv_"  # IV size should match block size (16 bytes)
    data = b"This is a plaintext message for testing."

    print("Original Data:", data)

    ecb_cipher, ecb_decrypted = encrypt_decrypt(modes.ECB(), key, iv, data)
    print("ECB Ciphertext:", ecb_cipher)
    print("ECB Decrypted:", ecb_decrypted)

    cbc_cipher, cbc_decrypted = encrypt_decrypt(modes.CBC(iv), key, iv, data)
    print("CBC Ciphertext:", cbc_cipher)
    print("CBC Decrypted:", cbc_decrypted)

    cfb_cipher, cfb_decrypted = encrypt_decrypt(modes.CFB(iv), key, iv, data)
    print("CFB Ciphertext:", cfb_cipher)
    print("CFB Decrypted:", cfb_decrypted)

if __name__ == "__main__":
    main()

Original Data: b'This is a plaintext message for testing.'
ECB Ciphertext: b'\xcamQ\xc1\xe5\x84\xe9\xa1\xbdSa\xa6\xe4l\x8cd\xdd\x7fm\x7f\x80M\x1a\xed3\xa3Q\xd4\xe1\xb1+u\x19\\\xb4k\xb8\xba\x1e\xab`x\x05\xca\x9e7\xa3\xce'
ECB Decrypted: b'This is a plaintext message for testing.'
CBC Ciphertext: b'\x91\xcd\x9a\xf3,=4,DJ\x94?d\x07\xe5\xecc\x93\xf4\x90\x8b\x1b\x02)\xa9\xc1\xff\xc3\xa8\xa0\xe3\xf0.\x7f^\x14a/\xf3\xf3\x8c\x8bMj1\xa5\xc5\x93'
CBC Decrypted: b'This is a plaintext message for testing.'
CFB Ciphertext: b'\x9a\x04\x9c\xa8\xfb\xfe\x02\xc1\xb6\xd9\xd3<J:\xc3\x7fm\xcb\x1f\x1f\xe9\xde\xb4{L|\xb4\x98\xd4\xdb`xRHG%2E\xf1QCD\xcf<[\xcf\xd2\xff'
CFB Decrypted: b'This is a plaintext message for testing.'
