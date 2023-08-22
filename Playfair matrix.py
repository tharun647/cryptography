def create_playfair_matrix(key):
    key = key.replace("J", "I")
    key = key.upper()
    key = "".join(dict.fromkeys(key))
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    matrix = []

    for char in key + alphabet:
        if char not in matrix:
            matrix.append(char)

    playfair_matrix = [matrix[i:i+5] for i in range(0, len(matrix), 5)]
    return playfair_matrix

def find_position(matrix, char):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col

def decrypt_playfair(message, key):
    playfair_matrix = create_playfair_matrix(key)
    decrypted_message = ""
    message = message.upper().replace("J", "I")

    for i in range(0, len(message), 2):
        char1 = message[i]
        char2 = message[i+1]

        row1, col1 = find_position(playfair_matrix, char1)
        row2, col2 = find_position(playfair_matrix, char2)

        if row1 == row2:
            decrypted_message += playfair_matrix[row1][(col1-1) % 5]
            decrypted_message += playfair_matrix[row2][(col2-1) % 5]
        elif col1 == col2:
            decrypted_message += playfair_matrix[(row1-1) % 5][col1]
            decrypted_message += playfair_matrix[(row2-1) % 5][col2]
        else:
            decrypted_message += playfair_matrix[row1][col2]
            decrypted_message += playfair_matrix[row2][col1]

    return decrypted_message

# Given Playfair-encoded message and key
encoded_message = "KXJEYUREBEZWEHEWRYTUHEYFSKREHEGOYFIWTTTUOLKSYCAJPOBOTEIZONTXBYBNTGONEYCUZWRGDSONSXBOUYWRHEBAAHYUSEDQ"
key = "PLAYFAIRCIPHER"

# Decrypt the message
decrypted_message = decrypt_playfair(encoded_message, key)
print("Decrypted Message:", decrypted_message)
