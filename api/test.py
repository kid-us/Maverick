from cryptography.fernet import Fernet
import base64

# Generate a random encryption key
encryption_key = Fernet.generate_key()

# Create a Fernet cipher object with the key
cipher = Fernet(encryption_key)

# Encrypt the email
email = "example@example.com"
encrypted_email = cipher.encrypt(email.encode())

# Encode the encrypted data using Base64
encoded_email = base64.urlsafe_b64encode(encrypted_email).decode()

# Decode the Base64 encoded data
decoded_email = base64.urlsafe_b64decode(encoded_email)

# Decrypt the email
decrypted_email = cipher.decrypt(decoded_email).decode()

print("Original Email:", email)
print("Encrypted Email:", encrypted_email)
print("Encoded Email:", encoded_email)
print("Decoded Email:", decoded_email)
print("Decrypted Email:", decrypted_email)
