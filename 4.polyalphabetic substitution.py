def polyalphabetic_cipher(text, key):
    encrypted_text = []
    key_index = 0
    for char in text:
        if char.isalpha():
            key_shift = ord(key[key_index % len(key)].upper()) - ord('A')
            if char.isupper():
                encrypted_char = chr((ord(char) - ord('A') + key_shift) % 26 + ord('A'))
            else:
                encrypted_char = chr((ord(char) - ord('a') + key_shift) % 26 + ord('a'))
            key_index += 1
        else:
            encrypted_char = char
        encrypted_text.append(encrypted_char)
    return ''.join(encrypted_text)
def main():
    plaintext = input("Enter the plaintext: ")
    key = input("Enter the key: ")
    encrypted_text = polyalphabetic_cipher(plaintext, key)
    print("Encrypted text:", encrypted_text)
if __name__ == "__main__":
    main()
