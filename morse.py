# Morse code dictionary
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ',': '--..--', '.': '.-.-.-', '?': '..--..', "'": '.----.',
    '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-',
    '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '/'
}
REVERSE_MORSE_CODE_DICT = {value: key for key, value in MORSE_CODE_DICT.items()}


# Function to encrypt plain text to Morse code
def morse_encrypt():
    message = input("Please enter the message to encrypt: ").upper()
    encrypted_message = ' '.join(MORSE_CODE_DICT.get(char, '') for char in message)
    return encrypted_message


# Function to decrypt Morse code to plain text
def morse_decrypt():
    message = input("Please enter the Morse code to decrypt (separate each code by space): ")
    decrypted_message = ''.join(REVERSE_MORSE_CODE_DICT.get(code, '') for code in message.split())
    return decrypted_message


# Main menu loop
while True:
    choice = input("Do you want to encrypt or decrypt Morse code? ").lower()
    if choice == "encrypt":
        print("Encrypted Morse Code:", morse_encrypt())
    elif choice == "decrypt":
        print("Decrypted Text:", morse_decrypt())
    else:
        print("Thanks for using me!")
        break
