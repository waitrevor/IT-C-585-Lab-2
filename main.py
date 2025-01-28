#Import required modules
import sys
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

# Define variables necessary for operation
key = b'YGEY5w/3a4pm60p/Lzzha+QDtqVWOk48'
iv = b'5c6bb191b09c9525'

#Read input data from STDIN
data = sys.stdin.buffer.read()
# Define the algorithm to be used
cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
# Create encryptor
encryptor = cipher.encryptor()
# Calculate ciphertext
ct = encryptor.update(data) + encryptor.finalize()
# Send ciphertext to STDOUT
print(ct)