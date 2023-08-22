import string
from random import shuffle
def generate_cipher_alphabet():
    alphabet = list(string.ascii_lowercase)
    shuffled_alphabet = alphabet.copy()
    shuffle(shuffled_alphabet)
    cipher_alphabet = dict(zip(alphabet, shuffled_alphabet))
    return cipher_alphabet
def encrypt(plaintext, cipher_alphabet):
    ciphertext = ''
    plaintext = plaintext.lower()
    for char in plaintext:
        if char.isalpha():
            ciphertext += cipher_alphabet[char]
        else:
            ciphertext += char
    return ciphertext
def decrypt(ciphertext, cipher_alphabet):
    plaintext = ''
    for char in ciphertext:
        if char.isalpha():
            for key, value in cipher_alphabet.items():
                if value == char:
                    plaintext += key
                    break
        else:
            plaintext += char
    
    return plaintext
cipher_alphabet = generate_cipher_alphabet()
print("Cipher Alphabet:", cipher_alphabet)
plaintext = input("enter text:")
ciphertext = encrypt(plaintext, cipher_alphabet)
print("Ciphertext:", ciphertext)
decrypted_plaintext = decrypt(ciphertext, cipher_alphabet)
print("Decrypted Plaintext:", decrypted_plaintext)
