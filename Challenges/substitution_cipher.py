def substitution_cipher_encrypt():
    # Ask for the substitution of 'a' to determine the shift
    start_char = input("What does 'a' map to? ").lower()
    if len(start_char) != 1 or not start_char.isalpha():
        print("Invalid input! Please provide a single alphabetical character.")
        return

    # Calculate the shift based on the starting character
    shift = (ord(start_char) - ord('a')) % 26
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    # Create the substitution key
    key = {alphabet[i]: alphabet[(i + shift) % 26] for i in range(26)}

    message = input("Please enter the message to encrypt: ")
    encrypted_message = ""

    for char in message:
        if char.isalpha():
            if char.islower():
                encrypted_message += key[char]
            else:
                encrypted_message += key[char.lower()].upper()
        else:
            encrypted_message += char

    return encrypted_message


def substitution_cipher_decrypt():
    print("Brute-forcing all possible shifts...")
    message = input("Please enter the message to decrypt: ")
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    # Test all 26 possible shifts
    possible_decryption = []
    for shift in range(26):
        reverse_key = {alphabet[(i + shift) % 26]: alphabet[i] for i in range(26)}
        decrypted_message = ""

        for char in message:
            if char.isalpha():
                if char.islower():
                    decrypted_message += reverse_key[char]
                else:
                    decrypted_message += reverse_key[char.lower()].upper()
            else:
                decrypted_message += char

        possible_decryption.append(decrypted_message)

    # Output all possible decryptions
    print("All possible decryptions:")
    for i, decryption in enumerate(possible_decryption, 1):
        print(f"{i}: {decryption}")


while True:
    choice = input("Do you want to encrypt or decrypt ? ").lower()
    if choice == "encrypt":
        print("Encrypted message:", substitution_cipher_encrypt())
    elif choice == "decrypt":
        substitution_cipher_decrypt()
    else:
        print("Thanks for using the cipher!")
        break
