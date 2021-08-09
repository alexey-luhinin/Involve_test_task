'''Configurations'''
from enum import Enum

SECRET = 'SecretKey01'


class Currency(Enum):
    EUR = 978
    USD = 840
    RUB = 643


if __name__ == '__main__':
    print(Currency.EUR.value)
