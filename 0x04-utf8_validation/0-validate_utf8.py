#!/usr/bin/python3
"""
Module to validate UTF-8 encoding.
"""


def validUTF8(data):
    """
    Validates if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list): A list of integers representing the data set.

    Returns:
        bool: True if the data is valid UTF-8 encoding, False otherwise.
    """
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Masks to check the most significant bits
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for num in data:
        # Get only the 8 least significant bits of num
        byte = num & 0xFF

        if num_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            if (byte & mask1) == 0:  # 1-byte character
                continue
            elif (byte & 0xE0) == 0xC0:  # 2-byte character
                num_bytes = 1
            elif (byte & 0xF0) == 0xE0:  # 3-byte character
                num_bytes = 2
            elif (byte & 0xF8) == 0xF0:  # 4-byte character
                num_bytes = 3
            else:  # Invalid starting byte
                return False
        else:
            # Check that the byte is a continuation byte (10xxxxxx)
            if (byte & 0xC0) != 0x80:
                return False
            num_bytes -= 1

    # Ensure all characters have been fully processed
    return num_bytes == 0
