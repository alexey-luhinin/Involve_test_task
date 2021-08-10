'''Utils'''
from hashlib import sha256


def get_sha256(text: str) -> str:
    '''Converts text to sha256 hex'''
    encoded_text = text.encode()
    hexed = sha256(encoded_text)
    return hexed.hexdigest()
