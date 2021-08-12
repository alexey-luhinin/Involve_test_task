'''Tests for utils.py'''
import pytest
from utils import get_sha256


@pytest.mark.parametrize(
        'text, expected', [
            ('10.00:643:5:101SecretKey01',
             'e4580435a252d61ef91b71cb23ed7bee4d77de94ced36411526d2ce3b66ada8f'),
            ('12.34:643:advcash_rub:5:4126SecretKey01',
             'd5d4e060ed32c10f3f8f3f5e829f2f084a4144e01da97799cd7f0035ddf07b3f'),
        ]
)
def test_get_sha256(text, expected):
    '''Tests for get_sha256'''
    assert get_sha256(text) == expected
