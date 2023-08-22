from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dsa

def generate_dsa_keypair():
    private_key = dsa.generate_private_key(key_size=1024)
    return private_key, private_key.public_key()

def sign_message(private_key, message):
    return private_key.sign(message, hashes.SHA256())

def verify_signature(public_key, message, signature):
    try:
        public_key.verify(signature, message, hashes.SHA256())
        return True
    except:
        return False

def main():
    message = b"This is a message that needs to be signed."
    
    private_key, public_key = generate_dsa_keypair()
    signature = sign_message(private_key, message)
    
    print("Original Message:", message)
    print("Signature:", signature.hex())
    
    valid = verify_signature(public_key, message, signature)
    if valid:
        print("Signature is valid.")
    else:
        print("Signature is NOT valid.")

if __name__ == "__main__":
    main()


Original Message: b'This is a message that needs to be signed.'
Signature: 302e021500b0dfb11d8ee66ee73339fcdc5ad2668981c803a0021500c18148c232939889eacfd5e6ecc1e7aa59469ecd
Signature is valid.
