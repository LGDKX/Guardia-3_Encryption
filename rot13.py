def rot13_encrypt():
    message = input("Please enter the message : ")
    encrypted_message = ""
    for char in message:
        if char.isalpha():  # Encrypt only alphabetic characters
            if char.islower():
                # Calculate new character for lowercase letters
                new_char = chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
            else:
                # Calculate new character for uppercase letters
                new_char = chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
            encrypted_message += new_char
        else:
            # Keep non-alphabetic characters unchanged
            encrypted_message += char
    return encrypted_message


def rot13_decrypt():
    message = input("Please enter the message : ")
    decrypted_message = ""
    for char in message:
        if char.isalpha():  # Decrypt only alphabetic characters
            if char.islower():
                # Calculate new character for lowercase letters
                new_char = chr((ord(char) - ord('a') - 13) % 26 + ord('a'))
            else:
                # Calculate new character for uppercase letters
                new_char = chr((ord(char) - ord('A') - 13) % 26 + ord('A'))
            decrypted_message += new_char
        else:
            # Keep non-alphabetic characters unchanged
            decrypted_message += char
    return decrypted_message


choice = input("Do you want to encrypt or decrypt? ")

if choice.lower() == "encrypt":
    print(rot13_encrypt())
else:
    print(rot13_decrypt())
