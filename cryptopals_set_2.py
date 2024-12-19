def pkcs7_padding() -> bytes:
    data = bytes(input("Enter the string to be padded: "), 'utf-8')
    block_size = int(input("Enter the block size: "))

    if block_size <= 0 or block_size > 255:
        raise ValueError("Block size must be between 1 and 255.")

    pad_length = block_size - (len(data) % block_size)
    padding = bytes([pad_length] * pad_length)
    return data + padding


padded_data = pkcs7_padding()
print(padded_data)

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
        use = input("What do you want to do? \n 1)  \n 2)  \n 3) "
                    " \n 4)  \n 5) Exit \n Enter your choice : ")

        if use == "1":
            print("Creating it")
        elif use == "2":
            print("Creating it")
        elif use == "3":
            print("Creating it")
        elif use == "4":
            print("Creating it")
        elif use == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid number.")
