#######################################################################
# Importing base64 library in order to encrypt/decrypt base64 strings #
#######################################################################
import base64

#######################################################################
# Importing os library in order to interact with the Operating System #
#######################################################################

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
    #     encoded_message (base64-bytes): encrypted message #
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
    #     Different buffer size                             #
    #########################################################
    # Get the two buffers with proper input validation
    buffer1 = hex_bytes("Please enter the first buffer (hex): ")
    buffer2 = hex_bytes("Please enter the second buffer (hex): ")

    # Check if the buffers are of equal size
    if len(buffer1) != len(buffer2):
        print(f"Error: Buffers must be of equal size. Got {len(buffer1)} and {len(buffer2)} bytes.")
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
    #######################################################
    # Decrypt a hex string XOR'd with a single-byte key   #
    #                                                     #
    # Call:                                               #
    #     hex_bytes(): to get the ciphertext              #
    #     score_text(): to evaluate plaintext             #
    #     single_byte_xor(): to XOR with single-byte keys #
    #######################################################
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
                    "single byte XOR \n 4) Exit \n Enter your choice : ")

        if use == "1":
            hex_to_base64()
        elif use == "2":
            equal_size_xor()
        elif use == "3":
            decrypt_single_byte_xor()
        elif use == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid number.")


choice()
