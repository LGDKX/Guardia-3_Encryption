#######################################################################
# Importing base64 library in order to encrypt/decrypt base64 strings #
#######################################################################
import base64


'''
Function to encrypt a hex string into base64

Args:
    message (hex): message to be encrypted
    encoded_message (base64-bytes): encrypted message
    
Raises:
    ValueError: if the hex string is invalid
'''


def hex_to_base64():
    # Get hex input from user
    message = input("Enter the hex string to be converted to base64: ")

    try:
        # Convert hex to bytes
        byte_data = bytes.fromhex(message)

        # Encode the bytes to base64
        encoded_message = base64.b64encode(byte_data)

        # Decode base64 bytes to a string and print the result
        print("Base64 encoded string:", encoded_message.decode("utf-8"))

    except ValueError:
        print("Invalid hex string.")