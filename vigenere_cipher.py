def vigenere_cipher():
    # Alphabet for reference
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    def process_text(text):
        """Convert text to uppercase and remove non-alphabetic characters"""
        return ''.join(filter(str.isalpha, text.upper()))
    
    def encrypt(plaintext, key):
        """Encrypt plaintext using Vigenère cipher"""
        plaintext = process_text(plaintext)
        key = process_text(key)
        if not key:
            raise ValueError("Key cannot be empty!")
        
        # Repeat key to match plaintext length
        key_repeated = (key * (len(plaintext) // len(key) + 1))[:len(plaintext)]
        
        ciphertext = []
        for p, k in zip(plaintext, key_repeated):
            # Shift calculation: (P + K) mod 26
            shift = (ord(p) + ord(k)) % 26
            ciphertext.append(chr(shift + ord('A')))
        return ''.join(ciphertext)
    
    def decrypt(ciphertext, key):
        """Decrypt ciphertext using Vigenère cipher"""
        ciphertext = process_text(ciphertext)
        key = process_text(key)
        if not key:
            raise ValueError("Key cannot be empty!")
        
        # Repeat key to match ciphertext length
        key_repeated = (key * (len(ciphertext) // len(key) + 1))[:len(ciphertext)]
        
        plaintext = []
        for c, k in zip(ciphertext, key_repeated):
            # Shift calculation: (C - K) mod 26
            shift = (ord(c) - ord(k)) % 26
            plaintext.append(chr(shift + ord('A')))
        return ''.join(plaintext)
    
    # User interaction
    print("\n=== Vigenère Cipher ===")
    while True:
        print("\nOptions:")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        choice = input("Select option (1/2/3): ").strip()
        
        if choice == '1':
            plaintext = input("Enter plaintext: ")
            key = input("Enter key: ")
            try:
                encrypted = encrypt(plaintext, key)
                print(f"\nEncrypted: {encrypted}")
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == '2':
            ciphertext = input("Enter ciphertext: ")
            key = input("Enter key: ")
            try:
                decrypted = decrypt(ciphertext, key)
                print(f"\nDecrypted: {decrypted}")
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == '3':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please try again.")

# Run the cipher
if __name__ == "__main__":
    vigenere_cipher()
