#!/usr/bin/python3
"""
UTF-8 VALIDATION
"""


def char_bytes_len(one_byte):
    """
    Return the number of bytes this character codes for

    A continuation returns None

    A single-byte character starts with = '0b0'
    A two-byte character starts with = '0b110'
    A three-byte character starts with = '0b1110'
    A four-byte character starts with = '0b11110'

    UTF-8 uses only 1-4 byte to encode characters
    """
    # Check if one_byte starts with '0b0'
    if one_byte >> 7 == 0b0:
        return 1    # A single-byte character

    bit_len = 5
    byte_count = 0b110

    while bit_len > 0:
        # Check if one_byte starts with `byte_count` binary value
        if one_byte >> bit_len == byte_count:
            return 7 - bit_len
        else:
            bit_len -= 1
            byte_count = (byte_count << 1) + 0b10

    # print("Could not find len of expected characters")  # test
    return None


def is_continuation_byte(one_byte):
    """
    Return True is a byte starts with 10
    """
    if one_byte >> 6 == 0b10:
        return True
    return False


def validUTF8(data):
    """
    Determine if a given data set represents a valid UTF-8 encoding.

    Return True if data is a valid UTF-8 encoding, else return False

    Sample data:
    data = [128, 323, 424]

    Each data set is a list of integers.
    The data set can contain multiple characters
    The data will be represented by a list of integers
    Each integer represents 1 byte of data, therefore you only need to
    handle the 8 least significant bits of each integer

    - CONCEPT -
    For a Single-byte character:
        * The byte starts with a `0`
        * It represents a single character in Unicode character set
    For a Two-byte character:
        * The byte starts with a `110`
    For a Three-byte character:
        * The byte starts with a `1110`
    For a continuation byte:
        * The byte starts with `10`
    Note: UTF-8 encodes character in 1 to 4 bytes and not more.
    """
    if not isinstance(data, list):
        return False

    bytes_left = 0  # the number of bytes to access
    for num in data:
        if not isinstance(num, int):
            return False

        if bytes_left:
            # Traverse through remaining bytes
            if not is_continuation_byte(num):
                # print(f"[{num}]: Continuation byte expected")     # test
                return False
            # print(f"[{num}]: Continuation byte gotten") # test
            bytes_left = bytes_left - 1
            continue

        # Get only the least significant byte
        one_byte = num & 0xFF

        # Get the total number of bytes expected
        num_char = char_bytes_len(one_byte)
        if not num_char:
            # print("Invalid byte")
            return False
        # print("[{}]: Total char len: {}".format(num, num_char))    # test

        if num_char > 4:
            # UTF-8 encodes a character using 1 to 4 bytes only
            # print("UTF-8 encodes a character using 1 to 4 bytes only")
            return False

        if num_char > 1:
            bytes_left = num_char - 1
            # print("Need to traverse {} more\
            # continuation bytes".format(bytes_left)) # test

    if bytes_left:
        # Did not traverse all the required continuation bytes
        # print(f"Did not traverse all continuation bytes")   # test
        return False

    return True
