from sympy import gcd, mod_inverse
import random

# RSA Key generation for simplicity
def generate_keys():
    # Toy primes for simplicity. Use proper primes in real scenarios.
    p, q = 61, 53  
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 17
    d = mod_inverse(e, phi)
    return (n, e), d

# Encryption function
def encrypt(public_key, plaintext):
    n, e = public_key
    return pow(plaintext, e, n)

public_key, private_key = generate_keys()
n, e = public_key

# Let's select a plaintext P that's a factor of n for demonstration.
P = n // 53  
C = encrypt(public_key, P)

# Attack using the knowledge that P is a factor of n
factor = gcd(P - pow(C, e, n), n)

print(f"Factor derived from attack: {factor}")
print(f"Private key derived from attack: {mod_inverse(e, (factor - 1) * (n // factor - 1))}")

# Note: This is a basic demonstration. In real-world scenarios, factors and parameters are much larger and require more computation.
Factor derived from attack: 61
Private key derived from attack: 2753
