from cryptography.fernet import Fernet

# Generate and save a key
key = Fernet.generate_key()
with open('secret.key', 'wb') as key_file:
    key_file.write(key)
