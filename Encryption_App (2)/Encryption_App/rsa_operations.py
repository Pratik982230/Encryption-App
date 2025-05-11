# rsa_operations.py
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def generate_rsa_keypair():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()

    with open('keys/rsa_private.pem', 'wb') as f:
        f.write(private_key)

    with open('keys/rsa_public.pem', 'wb') as f:
        f.write(public_key)

    print("RSA Keypair generated and saved to keys/rsa_private.pem and keys/rsa_public.pem.")

def rsa_encrypt(message):
    with open('keys/rsa_public.pem', 'rb') as f:
        public_key = RSA.import_key(f.read())
    
    cipher = PKCS1_OAEP.new(public_key)
    encrypted_message = cipher.encrypt(message.encode('utf-8'))
    return encrypted_message

def rsa_decrypt(encrypted_message):
    with open('keys/rsa_private.pem', 'rb') as f:
        private_key = RSA.import_key(f.read())
    
    cipher = PKCS1_OAEP.new(private_key)
    decrypted_message = cipher.decrypt(encrypted_message).decode('utf-8')
    return decrypted_message
