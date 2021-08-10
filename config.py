'''Configurations'''
import os
from pathlib import Path
from enum import Enum
from loguru import logger

log_dir = Path.cwd() / '.log'

if not log_dir.exists():
    os.mkdir(log_dir)

logger.add(".log/log.log")

SECRET = 'SecretKey01'
ERROR_MESSAGE = 'Something went wrong...'


class Currency(Enum):
    '''Currency'''
    EUR = 978
    USD = 840
    RUB = 643
