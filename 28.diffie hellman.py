def mod_pow(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp //= 2
        base = (base * base) % mod
    return result

q = 23  # Prime modulus
a = 5   # Public base
privateA = 6  # Alice's private key
privateB = 15  # Bob's private key

# Alice computes A = a^privateA mod q
A = mod_pow(a, privateA, q)

# Bob computes B = a^privateB mod q
B = mod_pow(a, privateB, q)

# Both Alice and Bob can compute the shared secret key
secretA = mod_pow(B, privateA, q)
secretB = mod_pow(A, privateB, q)

print("Shared secret key computed by Alice:", secretA)
print("Shared secret key computed by Bob:", secretB)

Shared secret key computed by Alice: 2
Shared secret key computed by Bob: 2
