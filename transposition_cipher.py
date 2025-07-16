def transposition_cipher():
    def process_text(text):
        """Remove spaces and convert to uppercase"""
        return ''.join(filter(str.isalpha, text.upper()))
    
    def pad_text(text, length):
        """Pad text with X to make it divisible by key length"""
        padding = (length - len(text) % length
        return text + 'X' * padding if padding != length else text
    
    def encrypt(plaintext, key):
        """Encrypt using columnar transposition"""
        plaintext = process_text(plaintext)
        key_order = sorted(range(len(key)), key=lambda k: key[k])
        
        # Pad text if needed
        padded_text = pad_text(plaintext, len(key))
        
        # Create grid
        grid = [padded_text[i:i+len(key)] for i in range(0, len(padded_text), len(key))]
        
        # Read columns in key order
        ciphertext = []
        for col in key_order:
            ciphertext.extend([row[col] for row in grid])
        return ''.join(ciphertext)
    
    def decrypt(ciphertext, key):
        """Decrypt columnar transposition cipher"""
        ciphertext = process_text(ciphertext)
        key_order = sorted(range(len(key)), key=lambda k: key[k])
        
        # Calculate rows needed
        rows = len(ciphertext) // len(key)
        
        # Reconstruct grid columns
        cols = []
        start = 0
        for col in key_order:
            cols.append((col, ciphertext[start:start+rows]))
            start += rows
        
        # Reorder columns to original
        cols.sort()
        
        # Read row-wise
        plaintext = []
        for row in range(rows):
            for col in range(len(key)):
                plaintext.append(cols[col][1][row])
        
        return ''.join(plaintext).rstrip('X')
    
    # User interaction
    print("\n=== Columnar Transposition Cipher ===")
    while True:
        print("\nOptions:")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        choice = input("Select option (1/2/3): ").strip()
        
        if choice == '1':
            plaintext = input("Enter plaintext: ")
            key = input("Enter key (word or numbers): ").upper()
            try:
                encrypted = encrypt(plaintext, key)
                print(f"\nEncrypted: {encrypted}")
            except Exception as e:
                print(f"Error: {e}")
        
        elif choice == '2':
            ciphertext = input("Enter ciphertext: ")
            key = input("Enter key (same as encryption): ").upper()
            try:
                decrypted = decrypt(ciphertext, key)
                print(f"\nDecrypted: {decrypted}")
            except Exception as e:
                print(f"Error: {e}")
        
        elif choice == '3':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    transposition_cipher()
