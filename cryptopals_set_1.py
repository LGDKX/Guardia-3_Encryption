#######################################################################
# Importing base64 library in order to encrypt/decrypt base64 strings #
#######################################################################
import base64

# Character frequency based on English text
CHAR_FREQUENCY = {'a': 8.2, 'b': 1.5, 'c': 2.8, 'd': 4.3, 'e': 12.7, 'f': 2.2, 'g': 2.0, 'h': 6.1, 'i': 7.0, 'j': 0.2,
                  'k': 0.8, 'l': 4.0, 'm': 2.4, 'n': 6.7, 'o': 7.5, 'p': 1.9, 'q': 0.1, 'r': 6.0, 's': 6.3, 't': 9.1,
                  'u': 2.8, 'v': 1.0, 'w': 2.4, 'x': 0.2, 'y': 2.0, 'z': 0.1, ' ': 19.0}


def hex_bytes(prompt):
    ##############################################################
    # Function to validate hex value and transform it into bytes #
    #                                                            #
    # Arg:                                                       #
    #     hex_input : the hex value                              #
    #                                                            #
    # Return:                                                    #
    #     decrypted hex value                                    #
    #                                                            #
    # Raises:                                                    #
    #     Invalid hex string                                     #
    ##############################################################
    while True:
        try:
            hex_input = input(prompt).strip()
            return bytes.fromhex(hex_input)
        except ValueError:
            print("Invalid hex string. Please enter a valid hexadecimal value.")


def hex_to_base64():
    #########################################################
    # Function to encrypt a hex string into base64          #
    #                                                       #
    # Args:                                                 #
    #     message (hex): message to be encrypted            #
    #     encoded_message (base64-bytes): encoded message   #
    #                                                       #
    # Call:                                                 #
    #     hex_bytes()                                       #
    #     base64 library : to encode message                #
    #                                                       #
    # Raises:                                               #
    #     ValueError: if the hex string is invalid          #
    #########################################################

    # Get hex input from user
    message = hex_bytes("Enter the hex string to be converted to base64: ")

    # Encode the bytes to base64
    encoded_message = base64.b64encode(message)

    # Decode base64 bytes to a string and print the result
    print("Base64 encoded string:", encoded_message.decode("utf-8"))


def equal_size_xor():
    #########################################################
    # XOR two equal-length buffers and return the result    #
    #                                                       #
    # Args:                                                 #
    #     buffer1 (bytes): The first buffer                 #
    #     buffer2(bytes): The second buffer                 #
    #                                                       #
    # Call:                                                 #
    #     hex_bytes()                                       #
    #                                                       #
    # Raises:                                               #
    #     SizeError : If the buffers are of different size  #
    #########################################################
    # Get the two buffers with proper input validation
    buffer1 = hex_bytes("Please enter the first buffer (hex): ")
    buffer2 = hex_bytes("Please enter the second buffer (hex): ")

    # Check if the buffers are of equal size
    if len(buffer1) != len(buffer2):
        print(f"SizeError: Buffers must be of equal size. Got {len(buffer1)} and {len(buffer2)} bytes.")
        return

    # Perform XOR
    xor_result = bytes(b1 ^ b2 for b1, b2 in zip(buffer1, buffer2))

    # Print the result in hexadecimal
    print("XOR result (hex):", xor_result.hex())


def score_text(text):
    ###############################################################
    # Function to score text based on English character frequency #
    #                                                             #
    # Arg:                                                        #
    #     text : plaintext to score                               #
    #                                                             #
    # Call:                                                       #
    #     CHAR_FREQUENCY dictionary                               #
    #                                                             #
    # Return:                                                     #
    #     score (float): Sum of character frequencies             #
    ###############################################################
    return sum(CHAR_FREQUENCY.get(chr(byte).lower(), 0) for byte in text)


def single_byte_xor(ciphertext, key):
    ##################################################
    # XOR a ciphertext with a single-byte key        #
    #                                                #
    # Args:                                          #
    #     ciphertext (bytes): The encoded message    #
    #     key (int): The single-byte key to XOR with #
    #                                                #
    # Return:                                        #
    #     decrypted (bytes): Resulting plaintext     #
    ##################################################
    return bytes([byte ^ key for byte in ciphertext])


def decrypt_single_byte_xor():
    #################################################################################
    # Decrypt a hex string XOR'd with a single-byte key                             #
    #                                                                               #
    # Call:                                                                         #
    #     hex_bytes():                                                              #
    #     score_text():                                                             #
    #     single_byte_xor():                                                        #
    #                                                                               #
    # Raises:                                                                       #
    #     FileNotFoundError: If the specified file path is invalid.                 #
    #     ValueError: If the input hex string cannot be parsed.                     #
    #     UnicodeDecodeError: If the plaintext contains invalid Unicode characters. #
    #################################################################################
    # Prompt the user to specify a file or single input
    input_path = input("Enter a file path or press Enter to input a single hex string: ").strip()

    # Function to decrypt a single line
    def process_line(hex_string):
        best_score = 0
        best_key = None
        best_plaintext = None

        # Try every possible single-byte key (0–255)
        for key in range(256):
            plaintext = single_byte_xor(hex_string, key)
            try:
                # Score the plaintext based on English character frequency
                score = score_text(plaintext)
                if score > best_score:
                    best_score = score
                    best_key = key
                    best_plaintext = plaintext
            except UnicodeDecodeError:
                # Ignore invalid plaintexts
                continue

        return best_key, best_plaintext

    # Check if input is a file path
    if input_path:
        try:
            with open(input_path, 'r') as file:
                print("Processing file...")
                for line_number, line in enumerate(file, start=1):
                    line = line.strip()
                    try:
                        # Use hex_bytes to validate and parse each line
                        hex_string = bytes.fromhex(line)
                        key, plaintext = process_line(hex_string)
                        print(f"Line {line_number}: {line}")
                        print(f"Key: {key} (character: {chr(key)})")
                        print(f"Decrypted message: {plaintext.decode('utf-8', errors='ignore')}\n")
                    except ValueError:
                        print(f"Skipping invalid hex line {line_number}: {line}")
        except FileNotFoundError:
            print("File not found. Please enter a valid file path.")
    else:
        # Use hex_bytes to validate and parse a single input
        hex_string = hex_bytes("Enter the XOR'd hex string: ")
        key, plaintext = process_line(hex_string)
        print(f"Key: {key} (character: {chr(key)})")
        print(f"Decrypted message: {plaintext.decode('utf-8', errors='ignore')}")


def repeating_key_xor():
    ############################################################
    # Encrypt text using repeating-key XOR                     #
    #                                                          #
    # Args:                                                    #
    #     plaintext (str): The text to encrypt                 #
    #     key (str): The repeating key for encryption          #
    #                                                          #
    # Call:                                                    #
    #     input(): To get plaintext and key from the user      #
    #                                                          #
    # Return:                                                  #
    #     ciphertext (str): The encrypted text in hex format   #
    #                                                          #
    # Raises:                                                  #
    #      KeyNotFound : If the key is empty                   #
    ############################################################

    # Prompt the user for plaintext
    plaintext = input("Enter the plaintext to encrypt: ").strip()

    # Prompt the user for the key
    key = input("Enter the encryption key: ").strip()

    if not key:
        print("KeyNotFound: Key cannot be empty.")
        return

    # Encrypt using repeating-key XOR
    ciphertext = bytes([ord(plaintext[i]) ^ ord(key[i % len(key)]) for i in range(len(plaintext))])

    # Convert ciphertext to hexadecimal and display
    print("Ciphertext (hex):", ciphertext.hex())


def hamming_distance(string1, string2):
    ##########################################################################
    # Calculate the hamming distance of binary strings (1+1=0, 0+0=1, 1+0=1) #
    #                                                                        #
    # Args:                                                                  #
    #     string1: The first string                                          #
    #     string2: The second string                                         #
    #                                                                        #
    # Return:                                                                #
    #     result (float): Hamming distance value                             #
    #                                                                        #
    # Raises:                                                                #
    #      ValueError : If the strings are not of equal size                 #
    ##########################################################################
    if len(string1) != len(string2):
        raise ValueError("Strings must be of equal length.")

    result = sum(c1 != c2 for c1, c2 in zip(string1, string2))
    return result


def hamming_debug():
    ##########################################
    # Debug hamming_distance()               #
    #                                        #
    # Args:                                  #
    #     string1: The first string          #
    #     string2: The second string         #
    #                                        #
    # Call:                                  #
    #     hamming_distance()                 #
    #                                        #
    # Raises:                                #
    #      KeyNotFound : If the key is empty #
    ##########################################
    string1 = ''.join(format(ord(char), '08b') for char in input("Enter the first string: "))
    string2 = ''.join(format(ord(char), '08b') for char in input("Enter the second string: "))
    result = hamming_distance(string1, string2)
    print(f"Hamming distance: {result}")


def key_size():
    ##############################################
    # Determine key size for challenge 6         #
    #                                            #
    # Args:                                      #
    #     string1: The first string              #
    #     string2: The second string             #
    #     result : The hamming distance          #
    #     final : The normalized value           #
    #                                            #
    # Call:                                      #
    #     hamming_distance()                     #
    #                                            #
    # Raises:                                    #
    #      LowData : In case of string too short #
    ##############################################
    # Read the Base64 file and decode it
    with open(input("Please enter the file path: "), "r") as file:
        base64_content = file.read()
        binary_data = base64.b64decode(base64_content)

    # Convert binary data to a binary string
    binary_string = ''.join(format(byte, '08b') for byte in binary_data)

    final_values = []

    for i in range(2, 40):
        # Extract the first and last i bits
        string1 = binary_string[:i * 8]  # Convert to bit length
        string2 = binary_string[-i * 8:]  # Convert to bit length

        if len(string1) < i * 8 or len(string2) < i * 8:
            print(f"LowData: Insufficient data for key size {i}")
            continue

        result = hamming_distance(string1, string2)
        # Normalize the hamming distance
        final = result / i
        # Append the result to the list
        final_values.append((i, final))
        print(f"For i = {i}, the normalized key size is: {final}")
        print("--------------------------------------------------")

    # Find the best key (lowest normalized value)
    best_key_size, smallest_final = min(final_values, key=lambda x: x[1])
    print(f"\nThe best key size is: {best_key_size} with the smallest normalized Hamming distance: {smallest_final}")


def choice():
    ################################################
    # Allow the user to choose the function to use #
    #                                              #
    # Call:                                        #
    #     hex_to_base64()                          #
    #     equal_size_xor()                         #
    #     decrypt_single_byte_xor()                #
    #                                              #
    # Raises                                       #
    #     Invalid input                            #
    ################################################
    while True:
        use = input("What do you want to do? \n 1) Hex to base64 \n 2) XOR two equal-length buffers \n 3) Decrypt a "
                    "single byte XOR \n 4) Repeating key XOR \n 5) Exit \n Enter your choice : ")

        if use == "1":
            hex_to_base64()
        elif use == "2":
            equal_size_xor()
        elif use == "3":
            decrypt_single_byte_xor()
        elif use == "4":
            repeating_key_xor()
        elif use == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid number.")


key_size()
