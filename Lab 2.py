import string

ALPHABET = string.ascii_lowercase


def validate_key(key):
    key = key.lower()
    return len(key) == 26 and key.isalpha() and len(set(key)) == 26


def encrypt(plaintext, key):
    key = key.lower()
    result = []

    for char in plaintext:
        if char.isalpha():
            index = ALPHABET.index(char.lower())
            encrypted = key[index]
            result.append(encrypted.upper() if char.isupper() else encrypted)
        else:
            result.append(char)

    return ''.join(result)


def decrypt(ciphertext, key):
    key = key.lower()
    reverse_map = {key[i]: ALPHABET[i] for i in range(26)}
    result = []

    for char in ciphertext:
        if char.isalpha():
            decrypted = reverse_map[char.lower()]
            result.append(decrypted.upper() if char.isupper() else decrypted)
        else:
            result.append(char)

    return ''.join(result)


# --- Main Program ---
print("=== Monoalphabetic Substitution Cipher ===")
print("Standard Alphabet:", ALPHABET)

key = input("Enter your 26-letter secret key: ").strip()
plaintext = input("Enter the text to encrypt: ")

if not validate_key(key):
    print("Error: Key must contain exactly 26 unique alphabetic characters.")
else:
    ciphertext = encrypt(plaintext, key)
    decrypted = decrypt(ciphertext, key)

    print("\n[+] Encrypted Text:", ciphertext)
    print("[+] Decrypted Text:", decrypted)