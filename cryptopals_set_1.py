#######################################################################
# Importing base64 library in order to encrypt/decrypt base64 strings #
#######################################################################
import base64


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


equal_size_xor()
