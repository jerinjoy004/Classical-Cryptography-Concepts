def prepare_text(text):
    # Remove non-alphabets and convert to uppercase
    return ''.join(filter(str.isalpha, text.upper()))

def vigenere_encrypt(plaintext, keyword):
    plaintext = prepare_text(plaintext)
    keyword = prepare_text(keyword)
    if not keyword:
        raise ValueError("Keyword cannot be empty!")
    
    # Repeat keyword to match plaintext length
    expanded_key = (keyword * (len(plaintext) // len(keyword) + 1))[:len(plaintext)]
    
    ciphertext = []
    for p_char, k_char in zip(plaintext, expanded_key):
        # Convert letters to 0-25 values
        p_num = ord(p_char) - ord('A')
        k_num = ord(k_char) - ord('A')
        # Apply Vigenère formula
        c_num = (p_num + k_num) % 26
        ciphertext.append(chr(c_num + ord('A')))
    
    return ''.join(ciphertext)

def vigenere_decrypt(ciphertext, keyword):
    ciphertext = prepare_text(ciphertext)
    keyword = prepare_text(keyword)
    if not keyword:
        raise ValueError("Keyword cannot be empty!")
    
    expanded_key = (keyword * (len(ciphertext) // len(keyword) + 1))[:len(ciphertext)]
    
    plaintext = []
    for c_char, k_char in zip(ciphertext, expanded_key):
        c_num = ord(c_char) - ord('A')
        k_num = ord(k_char) - ord('A')
        p_num = (c_num - k_num) % 26
        plaintext.append(chr(p_num + ord('A')))
    
    return ''.join(plaintext)

# Main Program
if __name__ == "__main__":
    print("\n=== Polyalphabetic Cipher (Vigenère) ===")
    
    # User input
    plaintext = input("Enter plaintext: ")
    keyword = input("Enter keyword: ")
    
    # Encrypt
    ciphertext = vigenere_encrypt(plaintext, keyword)
    print("\nEncrypted:", ciphertext)
    
    # Optional decryption
    decrypt_choice = input("\nDecrypt the ciphertext? (y/n): ").lower()
    if decrypt_choice == 'y':
        decrypted = vigenere_decrypt(ciphertext, keyword)
        print("Decrypted:", decrypted)
    else:
        print("\nExiting...")
