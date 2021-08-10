'''Payments handler'''
from typing import List
import requests
from utils import get_sha256
from config import SECRET, ERROR_MESSAGE


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

    full_request = {**fields}

    signed_data = add_sign(required_fields, full_request)

    response = requests.post(
        url='https://core.piastrix.com/bill/create',
        json=signed_data,
    )

    if response.status_code == 200:
        data_json = response.json().get('data')
        try:
            data_json['method'] = 'GET'
            data_json['action'] = data_json['url']
            del data_json['url']
        except TypeError as error:
            print(error)
            return {'error': ERROR_MESSAGE}

        return data_json

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
                print(error)
                return {'error': ERROR_MESSAGE}

            return data_json

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
