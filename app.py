'''Views'''
import requests
from typing import List
from flask import Flask, render_template, request, jsonify
from forms import PayForm
from config import SECRET, Payment, Currency
from utils import list_to_str, get_sha256

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    form = PayForm()
    if request.method == 'POST':
        user_request = request.get_json()
        currency = user_request['currency']

        if currency == str(Currency.EUR.value):
            eur_payment = Payment(
                uri='https://pay.piastrix.com/en/pay',
                required_fields=['amount', 'currency',
                                 'shop_id', 'shop_order_id']
            )

            data = add_sign(eur_payment.required_fields, user_request)
            data['url'] = eur_payment.uri
            data['method'] = 'POST'

            return jsonify(data)

        if currency == str(Currency.USD.value):
            usd_payment = Payment(
                uri='',
                required_fields=['shop_amount', 'shop_currency',
                                 'shop_id', 'shop_order_id',
                                 'payer_currency']
            )

            data = add_sign(usd_payment.required_fields, user_request)

            response = requests.post(
                url='https://core.piastrix.com/bill/create',
                json=data,
            )

            data_json = response.json()['data']
            data_json['method'] = 'GET'
            return jsonify(data_json)
        
        if currency == str(Currency.RUB.value):
            pass

    return render_template('index.html', form=form)


def add_sign(required_fields: List[str], user_request: dict) -> dict:
    '''Returns dictionary result which contains user request data + sign'''
    keys_sorted = sorted(required_fields)
    values = [user_request.get(key) for key in keys_sorted]
    sign = list_to_str(values) + SECRET
    sign_hashed = get_sha256(sign)

    data = dict(zip(keys_sorted, values))
    data['sign'] = sign_hashed

    result = {**user_request, **data}

    return result


if __name__ == '__main__':
    app.run(debug=True)
