# References:  https://www.pythoncentral.io/hashing-files-with-python

import hashlib
import time

def get_md5_checksum(filename, blocksize=65536):
    """ Given the name of a file, return its md5 hash value

    Args:
        filename (str): File Name
        blocksize (int, optional): Block size to use for the file buffer.
                                   Defaults to 65536.

    Returns:
        str: md5 hash value
    """
    hash = hashlib.md5()
    with open(filename, 'rb') as f: 
        buffer = f.read(blocksize)
        while buffer:
            hash.update(buffer)     
            buffer = f.read(blocksize)  
    return hash.hexdigest()


def get_sha256_checksum(filename, blocksize=65536):
    """ Given the name of a file, return its sha256 hash value

    Args:
        filename (str): File Name
        blocksize (int, optional): Block size to use for the file buffer.
                                   Defaults to 65536.

    Returns:
        str: sha256 hash value
    """
    hash = hashlib.sha256()
    with open(filename, 'rb') as f: 
        buffer = f.read(blocksize)
        while buffer:
            hash.update(buffer)     
            buffer = f.read(blocksize)  
    return hash.hexdigest()


def get_md5_for_text(text):
    """ Given text, return its md5 hash value

    Args:
        filename (str): Text for which md5 will be computed

    Returns:
        str: md5 hash value for given text
    """
    # Source: https://www.geeksforgeeks.org/python-convert-string-to-binary/
    #
    binary_text = ''.join(format(i, 'b') for i in bytearray(text, encoding ='utf-8'))
    hash = hashlib.md5(binary_text.encode())
    return hash.hexdigest()



