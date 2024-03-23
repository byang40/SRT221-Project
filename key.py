import secrets

secret_key = secrets.token_hex(16)  # Generate a random hexadecimal string of 16 bytes (32 characters)
print(secret_key)