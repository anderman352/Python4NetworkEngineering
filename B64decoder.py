# -*- coding: utf-8 -*-
"""
Created on Mon May 13 15:02:51 2024

@author: david
"""

import base64
import binascii

def decode_base64(data):
    try:
        return base64.b64decode(data).decode('utf-8')
    except binascii.Error:
        return None

def decode_hex(data):
    try:
        return bytes.fromhex(data).decode('utf-8')
    except ValueError:
        return None

def write_to_file(filename, data):
    with open(filename, 'w') as file:
        file.write(data)

def main():
    print("Please choose the type of encoding:")
    print("1. Base64")
    print("2. Hex")
    choice = input("Enter your choice (1/2): ")

    if choice not in ['1', '2']:
        print("Invalid choice. Exiting.")
        return

    encoded_data = input("Enter the encoded data: ")

    if choice == '1':
        decoded_data = decode_base64(encoded_data)
        encoding_type = 'Base64'
    else:
        decoded_data = decode_hex(encoded_data)
        encoding_type = 'Hex'

    if decoded_data is None:
        print(f"The data does not appear to be valid {encoding_type}. Are you sure you want to proceed?")
        proceed = input("Enter 'yes' to run anyway or 'no' to abort: ").lower()
        if proceed != 'yes':
            print("Aborting.")
            return

    print(f"Decoded {encoding_type} data: {decoded_data}")
    filename = decoded_data[:10] + '.txt' if decoded_data else 'output.txt'
    write_to_file(filename, f"Encoded {encoding_type} data: {encoded_data}\nDecoded data: {decoded_data}")
    print(f"Data has been written to {filename}")

if __name__ == "__main__":
    main()
bluet