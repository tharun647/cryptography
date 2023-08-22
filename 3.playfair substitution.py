def create_playfair_key(key):
    key = key.replace(" ", "").upper()
    key = key.replace("J", "I")  # Replace J with I
    key_set = set(key)
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    for ch in key_set:
        alphabet = alphabet.replace(ch, "")
    playfair_key = key + alphabet
    return playfair_key
def generate_playfair_matrix(key):
    playfair_matrix = [[0] * 5 for _ in range(5)]
    key = create_playfair_key(key)
    index = 0
    for row in range(5):
        for col in range(5):
            playfair_matrix[row][col] = key[index]
            index += 1
    return playfair_matrix
def find_char_location(matrix, char):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col

def playfair_encrypt(plain_text, key):
    matrix = generate_playfair_matrix(key)
    plain_text = plain_text.replace(" ", "").upper()
    plain_text = plain_text.replace("J", "I")
    i = 0
    while i < len(plain_text) - 1:
        if plain_text[i] == plain_text[i + 1]:
            plain_text = plain_text[:i + 1] + "X" + plain_text[i + 1:]
        i += 2
    if len(plain_text) % 2 != 0:
        plain_text += "X"
    encrypted_text = ""
    for i in range(0, len(plain_text), 2):
        char1, char2 = plain_text[i], plain_text[i + 1]
        row1, col1 = find_char_location(matrix, char1)
        row2, col2 = find_char_location(matrix, char2)
        
        if row1 == row2:
            encrypted_text += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            encrypted_text += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
        else:
            encrypted_text += matrix[row1][col2] + matrix[row2][col1]
    return encrypted_text
def playfair_decrypt(encrypted_text, key):
    matrix = generate_playfair_matrix(key)
    decrypted_text = ""
    for i in range(0, len(encrypted_text), 2):
        char1, char2 = encrypted_text[i], encrypted_text[i + 1]
        row1, col1 = find_char_location(matrix, char1)
        row2, col2 = find_char_location(matrix, char2)
        if row1 == row2:
            decrypted_text += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            decrypted_text += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
        else:
            decrypted_text += matrix[row1][col2] + matrix[row2][col1]
    
    return decrypted_text
key = input("enter key:")
plain_text = input("enter text:")
encrypted_text = playfair_encrypt(plain_text, key)
decrypted_text = playfair_decrypt(encrypted_text, key)

print("Plain text:", plain_text)
print("Encrypted text:", encrypted_text)
print("Decrypted text:", decrypted_text)
