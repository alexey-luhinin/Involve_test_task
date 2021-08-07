'''Configurations'''
from enum import Enum
from dataclasses import dataclass
from typing import List

SECRET = 'SecretKey01'


class Currency(Enum):
    EUR = 978
    USD = 840
    RUB = 643


@dataclass
class Payment:
    uri: str
    required_fields: List[str]


if __name__ == '__main__':
    print(Currency.EUR.value)
