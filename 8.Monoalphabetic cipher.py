def generate_cipher(keyword):
    keyword = ''.join(sorted(set(keyword), key=keyword.index))  # Remove duplicates while keeping the order
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    for char in keyword:
        alphabet = alphabet.replace(char, '')

    return keyword + alphabet

def encrypt(plain_text, cipher):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    encrypted_text = ""
    
    for char in plain_text.upper():
        if char in alphabet:
            encrypted_text += cipher[alphabet.index(char)]
        else:
            encrypted_text += char
            
    return encrypted_text

def main():
    keyword = "CIPHER"
    cipher_alphabet = generate_cipher(keyword)
    
    print("plain:   ", " ".join("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    print("cipher:  ", " ".join(cipher_alphabet))
    
    text = input("\nEnter plaintext to encrypt: ")
    encrypted_text = encrypt(text, cipher_alphabet)
    print("Encrypted text:", encrypted_text)

if __name__ == "__main__":
    main()
Enter plaintext to encrypt: hello world
Encrypted text: BEJJM WMQJH
