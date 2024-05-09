
#!/usr/bin/python3
'''UTF8 Validation module'''


def validUTF8(data):
    '''Function to perform validation'''
    num_bytes = 0

    for num in data:
        # Check if the current byte is a continuation byte
        if num & 0b11000000 == 0b10000000:
            # If it's not preceded by a leading byte, return False
            if num_bytes == 0:
                return False
            # Decrement the number of expected continuation bytes
            num_bytes -= 1
        else:
            # Check the number of bytes required for the current character
            if num_bytes > 0:
                return False
            # Determine the number of bytes required based on the leading byte
            if num & 0b10000000 == 0:
                num_bytes = 0
            elif num & 0b11100000 == 0b11000000:
                num_bytes = 1
            elif num & 0b11110000 == 0b11100000:
                num_bytes = 2
            elif num & 0b11111000 == 0b11110000:
                num_bytes = 3
            else:
                # Invalid leading byte
                return False

    # Check if there are any remaining continuation bytes
    if num_bytes > 0:
        return False

    return True

