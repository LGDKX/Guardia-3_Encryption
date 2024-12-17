def caesar_encrypt():
    message = input("Please enter the message : ")
    shift = int(input("Please enter the shift value : "))
    encrypted_message = ""
    for char in message:
        if char.isalpha():  # Encrypt only alphabetic characters
            if char.islower():
                # Calculate new character for lowercase letters
                new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                # Calculate new character for uppercase letters
                new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            encrypted_message += new_char
        else:
            # Keep non-alphabetic characters unchanged
            encrypted_message += char
    return encrypted_message


def caesar_decrypt():
    message = input("Please enter the message : ")
    possible_decryption = {}
    for shift in range(27):  # Test all shifts from 0 to 26
        decrypted_message = ""
        for char in message:
            if char.isalpha():  # Decrypt only alphabetic characters
                if char.islower():
                    # Calculate new character for lowercase letters
                    new_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
                else:
                    # Calculate new character for uppercase letters
                    new_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
                decrypted_message += new_char
            else:
                # Keep non-alphabetic characters unchanged
                decrypted_message += char
        # Store the decryption result with its shift
        possible_decryption[shift] = decrypted_message
    return possible_decryption


while True:
    choice = input("Do you want to encrypt or decrypt? ").lower()
    if choice == "encrypt":
        print(caesar_encrypt())
    elif choice == "decrypt":
        print(caesar_decrypt())
    else:
        print("Thanks for using me !")
        break
