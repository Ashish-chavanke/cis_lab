import numpy as np
from sympy import Matrix

def prepare_text(text, n):
    """Removes spaces/symbols and pads text with X to fit block size."""
    text = "".join([c.upper() for c in text if c.isalpha()])

    while len(text) % n != 0:
        text += "X"

    return text


def encrypt_hill(plaintext, key_matrix):
    n = key_matrix.shape[0]
    text = prepare_text(plaintext, n)

    ciphertext = ""

    for i in range(0, len(text), n):
        # Create column vector P
        block = [ord(c) - 65 for c in text[i:i+n]]
        P = np.array(block).reshape(n, 1)

        # Matrix multiplication C = K * P mod 26
        C = np.dot(key_matrix, P) % 26

        for val in C.flatten():
            ciphertext += chr(int(val) + 65)

    return ciphertext


def decrypt_hill(ciphertext, key_matrix):
    n = key_matrix.shape[0]

    # Calculate inverse matrix modulo 26
    try:
        inv_matrix = np.array(Matrix(key_matrix).inv_mod(26)).astype(int)
    except ValueError:
        return "Error: Key matrix is not invertible modulo 26."

    plaintext = ""

    for i in range(0, len(ciphertext), n):
        # Create column vector C
        block = [ord(c) - 65 for c in ciphertext[i:i+n]]
        C = np.array(block).reshape(n, 1)

        # Matrix multiplication P = K_inv * C mod 26
        P = np.dot(inv_matrix, C) % 26

        for val in P.flatten():
            plaintext += chr(int(val) + 65)

    return plaintext


# ---------------------------------------------------
# Hill Cipher - Custom 3x3 Key Matrix
# ---------------------------------------------------

print("=== Hill Cipher Tool ===")

# Custom 3x3 key matrix
K = np.array([
    [6, 24, 1],
    [13, 16, 10],
    [20, 17, 15]
])

message = "HELLO"

print("Key Matrix:")
print(K)

print("Plaintext:", message)

# Encryption
encrypted = encrypt_hill(message, K)

print("[+] Encrypted Text:", encrypted)

# Decryption
decrypted = decrypt_hill(encrypted, K)

print("[+] Decrypted Text:", decrypted)
