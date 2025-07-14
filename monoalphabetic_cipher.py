import random

def generate_key():
    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    shuffled = alphabet.copy()
    random.shuffle(shuffled)
    return dict(zip(alphabet, shuffled))

def monoalphabetic_encrypt(plaintext, key):
    ciphertext = []
    for char in plaintext.upper():
        if char.isalpha():
            ciphertext.append(key[char])
        else:
            ciphertext.append(char)
    return ''.join(ciphertext)

def monoalphabetic_decrypt(ciphertext, key):
    reverse_key = {v: k for k, v in key.items()}
    plaintext = []
    for char in ciphertext.upper():
        if char.isalpha():
            plaintext.append(reverse_key[char])
        else:
            plaintext.append(char)
    return ''.join(plaintext)

# Main Program
if __name__ == "__main__":
    # Generate a random key
    key = generate_key()
    print("\nGenerated Key (A→Z mapping):")
    for k, v in sorted(key.items()):
        print(f"{k} → {v}", end=" | ")
    
    # Take user input
    plaintext = input("\n\nEnter text to encrypt: ")
    
    # Encrypt
    ciphertext = monoalphabetic_encrypt(plaintext, key)
    print("\nEncrypted:", ciphertext)
    
    # Decrypt (optional)
    decrypt_choice = input("\nDecrypt the ciphertext? (y/n): ").lower()
    if decrypt_choice == 'y':
        decrypted = monoalphabetic_decrypt(ciphertext, key)
        print("Decrypted:", decrypted)
    else:
        print("\nExiting...")
