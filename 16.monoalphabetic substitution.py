import string
from collections import Counter

ENGLISH_FREQUENCIES = ['E', 'T', 'A', 'O', 'I', 'N', 'S', 'H', 'R', 'D', 'L', 'C', 'U', 'M', 'W', 'F', 'G', 'Y', 'P', 'B', 'V', 'K', 'J', 'X', 'Q', 'Z']

def decrypt_substitution(ciphertext, mapping):
    decrypted = ""
    for char in ciphertext:
        if char in mapping:
            decrypted += mapping[char]
        else:
            decrypted += char
    return decrypted

def frequency_analysis(ciphertext, n=10):
    counter = Counter(ciphertext)
    most_common = [item[0] for item in counter.most_common(len(ENGLISH_FREQUENCIES))]

    # Create possible mappings
    possible_mappings = []
    for i in range(n):
        mapping = {}
        for j, letter in enumerate(most_common):
            mapping[letter] = ENGLISH_FREQUENCIES[j]
        possible_mappings.append(mapping)

    plaintexts = [decrypt_substitution(ciphertext, mapping) for mapping in possible_mappings]
    return plaintexts

def main():
    ciphertext = input("Enter the ciphertext: ").upper()
    n = int(input("How many possible plaintexts do you want? "))

    plaintexts = frequency_analysis(ciphertext, n)
    for i, text in enumerate(plaintexts, 1):
        print(f"{i}. {text}")

if __name__ == "__main__":
    main()
Enter the ciphertext: hello world
How many possible plaintexts do you want? 5
1. AOEETINTSEH
2. AOEETINTSEH
3. AOEETINTSEH
4. AOEETINTSEH
5. AOEETINTSEH
