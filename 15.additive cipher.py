import string
from collections import Counter

# Known letter frequency in the English language
ENGLISH_FREQUENCIES = ['E', 'T', 'A', 'O', 'I', 'N', 'S', 'H', 'R', 'D', 'L', 'C', 'U', 'M', 'W', 'F', 'G', 'Y', 'P', 'B', 'V', 'K', 'J', 'X', 'Q', 'Z']

def decrypt_caesar(ciphertext, shift):
    alphabet = string.ascii_uppercase
    decrypted = ""

    for char in ciphertext:
        if char in alphabet:
            decrypted += alphabet[(alphabet.index(char) - shift) % 26]
        else:
            decrypted += char

    return decrypted

def frequency_analysis(ciphertext, n=10):
    counter = Counter(ciphertext)
    most_common = [item[0] for item in counter.most_common(n)]
    possible_shifts = []

    for common in most_common:
        for freq in ENGLISH_FREQUENCIES:
            shift = (ord(common) - ord(freq)) % 26
            if shift not in possible_shifts:
                possible_shifts.append(shift)

    plaintexts = []
    for shift in possible_shifts:
        plaintexts.append(decrypt_caesar(ciphertext, shift))

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
1. AXEEH PHKEW
2. PMTTW EWZTL
3. WTAAD LDGAS
4. KHOOR ZRUOG
5. EBIIL TLOIA
6. JGNNQ YQTNF
7. OLSSV DVYSK
8. DAHHK SKNHZ
9. NKRRU CUXRJ
10. ZWDDG OGJDV
11. HELLO WORLD
12. YVCCF NFICU
13. QNUUX FXAUM
14. IFMMP XPSME
15. SPWWZ HZCWO
16. BYFFI QILFX
17. CZGGJ RJMGY
18. URYYB JBEYQ
19. LIPPS ASVPH
20. XUBBE MEHBT
21. ROVVY GYBVN
22. GDKKN VNQKC
23. FCJJM UMPJB
24. TQXXA IADXP
25. MJQQT BTWQI
26. VSZZC KCFZR
