'''Utils'''
from hashlib import sha256
from typing import List


def get_sha256(text: str) -> str:
    '''Converts text to sha256 hex'''
    encoded_text = text.encode()
    hexed = sha256(encoded_text)
    return hexed.hexdigest()


def list_to_str(items: List[str], delimiter: str = ':') -> str:
    '''Concatenates the list into a string'''
    return delimiter.join(items)


if __name__ == '__main__':
    print(get_sha256('10.00:643:5:101SecretKey01'))
    print(list_to_str(['a', 'b', 'c']))
