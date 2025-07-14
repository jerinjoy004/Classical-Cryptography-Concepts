def prepare_text(text):
    # Remove non-alphabets, convert to uppercase, replace J with I
    text = ''.join(filter(str.isalpha, text.upper()))
    text = text.replace("J", "I")
    return text

def generate_key_matrix(key):
    key = prepare_text(key)
    # Remove duplicates while preserving order
    seen = set()
    key_no_duplicates = []
    for char in key:
        if char not in seen:
            seen.add(char)
            key_no_duplicates.append(char)
    # Fill remaining with alphabet (A-Z, excluding J)
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    for char in alphabet:
        if char not in seen:
            key_no_duplicates.append(char)
    # Split into 5x5 matrix
    key_matrix = [key_no_duplicates[i*5:(i+1)*5] for i in range(5)]
    return key_matrix

def find_position(matrix, char):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return (row, col)
    raise ValueError(f"Character {char} not found in matrix")

def playfair_encrypt(plaintext, key_matrix):
    plaintext = prepare_text(plaintext)
    # Pad with 'X' if odd length
    if len(plaintext) % 2 != 0:
        plaintext += 'X'
    ciphertext = []
    for i in range(0, len(plaintext), 2):
        a, b = plaintext[i], plaintext[i+1]
        row_a, col_a = find_position(key_matrix, a)
        row_b, col_b = find_position(key_matrix, b)
        # Same row: shift right
        if row_a == row_b:
            ciphertext.append(key_matrix[row_a][(col_a + 1) % 5])
            ciphertext.append(key_matrix[row_b][(col_b + 1) % 5])
        # Same column: shift down
        elif col_a == col_b:
            ciphertext.append(key_matrix[(row_a + 1) % 5][col_a])
            ciphertext.append(key_matrix[(row_b + 1) % 5][col_b])
        # Rectangle: swap columns
        else:
            ciphertext.append(key_matrix[row_a][col_b])
            ciphertext.append(key_matrix[row_b][col_a])
    return ''.join(ciphertext)

def playfair_decrypt(ciphertext, key_matrix):
    ciphertext = prepare_text(ciphertext)
    plaintext = []
    for i in range(0, len(ciphertext), 2):
        a, b = ciphertext[i], ciphertext[i+1]
        row_a, col_a = find_position(key_matrix, a)
        row_b, col_b = find_position(key_matrix, b)
        # Same row: shift left
        if row_a == row_b:
            plaintext.append(key_matrix[row_a][(col_a - 1) % 5])
            plaintext.append(key_matrix[row_b][(col_b - 1) % 5])
        # Same column: shift up
        elif col_a == col_b:
            plaintext.append(key_matrix[(row_a - 1) % 5][col_a])
            plaintext.append(key_matrix[(row_b - 1) % 5][col_b])
        # Rectangle: swap columns
        else:
            plaintext.append(key_matrix[row_a][col_b])
            plaintext.append(key_matrix[row_b][col_a])
    return ''.join(plaintext)

# Main Program
if __name__ == "__main__":
    # User input
    key = input("Enter the key: ")
    plaintext = input("Enter the plaintext: ")
    
    # Generate key matrix
    key_matrix = generate_key_matrix(key)
    print("\nKey Matrix (5x5):")
    for row in key_matrix:
        print(' '.join(row))
    
    # Encrypt
    ciphertext = playfair_encrypt(plaintext, key_matrix)
    print("\nEncrypted:", ciphertext)
    
    # Decrypt (optional)
    decrypt_choice = input("\nDecrypt the ciphertext? (y/n): ").lower()
    if decrypt_choice == 'y':
        decrypted = playfair_decrypt(ciphertext, key_matrix)
        print("Decrypted:", decrypted)
    else:
        print("\nExiting...")
