// static/js/script.js
document.getElementById('generate-rsa').addEventListener('click', async () => {
    const response = await fetch('/generate_rsa_keys', { method: 'POST' });
    const result = await response.json();
    alert(result.message);
});

document.getElementById('encrypt-btn').addEventListener('click', async () => {
    const message = document.getElementById('message-to-encrypt').value;
    const response = await fetch('/encrypt_message', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message })
    });
    const result = await response.json();
    document.getElementById('encrypted-message').innerText = `Encrypted: ${result.encrypted_message}`;
});

document.getElementById('decrypt-btn').addEventListener('click', async () => {
    const encrypted_message = document.getElementById('message-to-decrypt').value;
    const response = await fetch('/decrypt_message', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ encrypted_message })
    });
    const result = await response.json();
    document.getElementById('decrypted-message').innerText = `Decrypted: ${result.decrypted_message}`;
});

document.getElementById('generate-ecc').addEventListener('click', async () => {
    const response = await fetch('/generate_ecc_keys', { method: 'POST' });
    const result = await response.json();
    alert(result.message);
});

document.getElementById('sign-btn').addEventListener('click', async () => {
    const message = document.getElementById('message-to-sign').value;
    const response = await fetch('/sign_message', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message })
    });
    const result = await response.json();
    document.getElementById('signature').innerText = `Signature: ${result.signature}`;
});

document.getElementById('verify-btn').addEventListener('click', async () => {
    const message = document.getElementById('message-to-verify').value;
    const signature = document.getElementById('signature-to-verify').value;
    const response = await fetch('/verify_signature', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message, signature })
    });
    const result = await response.json();
    document.getElementById('verification-result').innerText = result.is_valid ? 'Signature is valid.' : 'Signature is invalid.';
});
