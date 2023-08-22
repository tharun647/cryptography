Write a C program for ciphertext has been generated with an affine cipher. The most frequent letter of the ciphertext is “B,” 
and the second most frequent letter of the ciphertext is “U.”Break this code.
PROGRAM :-
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None
def affine_decrypt(ciphertext, a, b):
    mod_inv = mod_inverse(a, 26)
    if mod_inv is None:
        return "Error: 'a' value is not valid (no modular inverse exists)"
    decryption = ""
    for char in ciphertext:
        if char.isalpha():
            shift = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr(((mod_inv * (ord(char) - shift - b)) % 26) + shift)
            decryption += decrypted_char
        else:
            decryption += char
    return decryption
ciphertext = "BUUKWZB BUBUBU"
most_frequent = "B"
second_most_frequent = "U"
a = (ord(second_most_frequent) - ord(most_frequent)) * mod_inverse(ord('T') - ord('E'), 26) % 26
b = (ord(second_most_frequent) - a * ord('T') - ord('E')) % 26
decrypted_message = affine_decrypt(ciphertext, a, b)
print("Decrypted Message:")
print(decrypted_message)
