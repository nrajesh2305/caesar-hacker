from hacker import *

encrypted_message = input("Enter the encrypted Caesar Cipher message to hack.\n")
encrypted_message = encrypted_message.upper()

for i in range(26):
    print(f"Key #{i}: " + decrypt_message(encrypted_message, i))