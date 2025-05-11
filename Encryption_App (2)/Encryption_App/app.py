# app.py
from flask import Flask, render_template, request, jsonify
from rsa_operations import generate_rsa_keypair, rsa_encrypt, rsa_decrypt
from ecc_operations import generate_ecc_keypair, ecc_sign, ecc_verify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_rsa_keys', methods=['POST'])
def generate_rsa_keys():
    generate_rsa_keypair()
    return jsonify({'message': 'RSA keypair generated.'})

@app.route('/encrypt_message', methods=['POST'])
def encrypt_message():
    message = request.json['message']
    encrypted_message = rsa_encrypt(message)
    return jsonify({'encrypted_message': encrypted_message.hex()})

@app.route('/decrypt_message', methods=['POST'])
def decrypt_message():
    encrypted_message = bytes.fromhex(request.json['encrypted_message'])
    decrypted_message = rsa_decrypt(encrypted_message)
    return jsonify({'decrypted_message': decrypted_message})

@app.route('/generate_ecc_keys', methods=['POST'])
def generate_ecc_keys():
    generate_ecc_keypair()
    return jsonify({'message': 'ECC keypair generated.'})

@app.route('/sign_message', methods=['POST'])
def sign_message():
    message = request.json['message']
    signature = ecc_sign(message)
    return jsonify({'signature': signature.hex()})

@app.route('/verify_signature', methods=['POST'])
def verify_signature():
    message = request.json['message']
    signature = bytes.fromhex(request.json['signature'])
    is_valid = ecc_verify(signature, message)
    return jsonify({'is_valid': is_valid})

if __name__ == '__main__':
    app.run(debug=True)
