'''Payments handler'''
from typing import List
import requests
from utils import get_sha256
from config import SECRET, ERROR_MESSAGE, logger
from models import Payment


def eur_handler(user_request: dict) -> dict:
    '''Eur handler'''
    required_fields = ['amount', 'currency',
                       'shop_id', 'shop_order_id']

    fields = {
        'shop_id': '5',
        'shop_order_id': '109'
    }

    full_request = {**user_request, **fields}

    signed_data = add_sign(required_fields, full_request)
    signed_data['method'] = 'POST'
    signed_data['action'] = 'https://pay.piastrix.com/en/pay'

    logging(full_request)

    insert_into_db(full_request)

    return signed_data


def usd_handler(user_request: dict) -> dict:
    '''Usd handler'''
    required_fields = ['shop_amount', 'shop_currency',
                       'shop_id', 'shop_order_id',
                       'payer_currency']

    fields = {
        'shop_id': '5',
        'shop_order_id': '109',
        'shop_amount': user_request['amount'],
        'shop_currency': '840',
        'payer_currency': user_request['currency'],
        'payer_account': 'support@piastrix.com'
    }

    full_request = {**user_request, **fields}

    signed_data = add_sign(required_fields, full_request)

    response = requests.post(
        url='https://core.piastrix.com/bill/create',
        json=signed_data,
    )

    if response.status_code == 200:
        data_json = response.json().get('data')
        if data_json:
            try:
                data_json['method'] = 'GET'
                data_json['action'] = data_json['url']
                del data_json['url']
            except TypeError as error:
                logger.warning(error)
                return {'error': ERROR_MESSAGE}

            logging(full_request)

            insert_into_db(full_request)

            return data_json

        logger.warning('Key "data" is not found!')
        return {'error': ERROR_MESSAGE}

    logger.warning('Status code: {}', response.status_code)
    return {'error': ERROR_MESSAGE}


def rub_handler(user_request: dict) -> dict:
    '''Rub handler'''
    required_fields = ['amount', 'currency',
                       'payway', 'shop_id', 'shop_order_id']

    fields = {
        'shop_id': '5',
        'shop_order_id': '109',
        'payway': 'advcash_rub'
    }

    full_request = {**user_request, **fields}

    signed_data = add_sign(required_fields, full_request)

    response = requests.post(
        url='https://core.piastrix.com/invoice/create',
        json=signed_data,
    )

    if response.status_code == 200:
        response_json = response.json().get('data')
        if response_json:
            try:
                data_json = response_json.get('data')
                data_json['method'] = response_json.get('method')
                data_json['action'] = response_json.get('url')
            except TypeError as error:
                logger.warning(error)
                return {'error': ERROR_MESSAGE}

            logging(full_request)

            insert_into_db(full_request)

            return data_json

        logger.warning('Key "data" is not found!')
        return {'error': ERROR_MESSAGE}

    logger.warning('Status code: {}', response.status_code)
    return {'error': ERROR_MESSAGE}


def add_sign(required_fields: List[str], user_request: dict) -> dict:
    '''Returns dictionary which contains user request data + sign'''
    keys_sorted = sorted(required_fields)
    values = [user_request.get(key, '') for key in keys_sorted]

    sign = ':'.join(values) + SECRET
    sign_hashed = get_sha256(sign)

    signed_data = dict(zip(keys_sorted, values))
    signed_data['sign'] = sign_hashed

    return {**user_request, **signed_data}


def logging(data: dict) -> None:
    '''Logging information to file'''
    logger.info('id: {}, currency: {}, amount: {}, description: {}',
                data['shop_order_id'],
                data['currency'],
                data['amount'],
                data['description'])


def insert_into_db(data: dict) -> None:
    '''Save information to database'''
    payment = Payment(
        currency=data['currency'],
        amount=data['amount'],
        description=data['description'],
        shop_order_id=data['shop_order_id']
    )

    try:
        payment.save()
    except Exception as error:
        logger.warning(error)
