def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x, y = extended_gcd(b, a % b)
        return gcd, y, x - (a // b) * y

def modular_inverse(e, phi):
    _, x, _ = extended_gcd(e, phi)
    return x % phi

def main():
    e = 31
    n = 3599

    # Find prime factors p and q
    p = 59
    q = 61

    # Calculate Euler's totient function φ(n)
    phi = (p - 1) * (q - 1)

    # Calculate private key d using modular inverse
    d = modular_inverse(e, phi)

    print("Private Key (d):", d)

if __name__ == "__main__":
    main()

Private Key (d): 3031
