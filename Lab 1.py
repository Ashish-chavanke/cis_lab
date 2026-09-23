def encrypt_caesar(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            shifted_char = chr(
                (ord(char) - ascii_offset + shift) % 26
                + ascii_offset
            )
            result += shifted_char
        else:
            result += char

    return result


def decrypt_caesar(text, shift):
    return encrypt_caesar(text, -shift)


# Interactive execution
print("=== Caesar Cipher Tool ===")

plaintext = input("Enter the text to encrypt: ")
key = int(input("Enter the shift value (integer): "))

encrypted_text = encrypt_caesar(plaintext, key)
print("\n[+] Encrypted Text:", encrypted_text)

decrypted_text = decrypt_caesar(encrypted_text, key)
print("[+] Decrypted Text:", decrypted_text)