# ecc_operations.py
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization, hashes

def generate_ecc_keypair():
    private_key = ec.generate_private_key(ec.SECP256R1())
    public_key = private_key.public_key()

    with open("keys/ecc_private.pem", "wb") as f:
        f.write(private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        ))

    with open("keys/ecc_public.pem", "wb") as f:
        f.write(public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ))

    print("ECC Keypair generated and saved to keys/ecc_private.pem and keys/ecc_public.pem.")

def ecc_sign(message):
    with open("keys/ecc_private.pem", "rb") as f:
        private_key = serialization.load_pem_private_key(f.read(), password=None)

    signature = private_key.sign(message.encode('utf-8'), ec.ECDSA(hashes.SHA256()))
    return signature

def ecc_verify(signature, message):
    with open("keys/ecc_public.pem", "rb") as f:
        public_key = serialization.load_pem_public_key(f.read())

    try:
        public_key.verify(signature, message.encode('utf-8'), ec.ECDSA(hashes.SHA256()))
        return True
    except:
        return False
