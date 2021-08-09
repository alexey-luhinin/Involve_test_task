'''Views'''
from typing import List
from flask import (
    Flask,
    render_template,
    request,
    jsonify,
    redirect,
    url_for,
    session
)
import requests
from config import SECRET, Payment, Currency
from forms import PayForm
from utils import list_to_str, get_sha256

app = Flask(__name__)
app.secret_key = 'test'


@app.route('/', methods=['GET', 'POST'])
def index():
    form = PayForm(request.form)
    if request.method == 'POST':
        user_request = request.get_json()
        amount = user_request['amount']
        currency = user_request['currency']

        if currency == str(Currency.EUR.value):

            required_fields = ['amount', 'currency',
                               'shop_id', 'shop_order_id']

            shop = {
                'shop_id': '5',
                'shop_order_id': '109'
            }

            full_request = {**user_request, **shop}

            data = add_sign(required_fields, full_request)
            data['method'] = 'POST'
            data['action'] = 'https://pay.piastrix.com/en/pay'
            return jsonify(data)

        if currency == str(Currency.USD.value):

            required_fields = ['shop_amount', 'shop_currency',
                               'shop_id', 'shop_order_id',
                               'payer_currency']

            shop = {
                'shop_id': '5',
                'shop_order_id': '109',
                'shop_amount': amount,
                'shop_currency': '840',
                'payer_currency': currency,
                'payer_account': 'support@piastrix.com'
            }

            full_request = {**shop}

            data = add_sign(required_fields, full_request)

            response = requests.post(
                url='https://core.piastrix.com/bill/create',
                json=data,
            )

            data_json = response.json().get('data')
            data_json['method'] = 'GET'
            data_json['action'] = data_json['url']
            del data_json['url']
            return jsonify(data_json)

        # if currency == str(Currency.RUB.value):
        #     pass

    return render_template('index.html', form=form)


def add_sign(required_fields: List[str], user_request: dict) -> dict:
    '''Returns dictionary result which contains user request data + sign'''
    keys_sorted = sorted(required_fields)
    print(keys_sorted)
    values = [user_request.get(key) for key in keys_sorted]
    sign = list_to_str(values) + SECRET
    sign_hashed = get_sha256(sign)

    data = dict(zip(keys_sorted, values))
    data['sign'] = sign_hashed

    result = {**user_request, **data}

    return result


if __name__ == '__main__':
    app.run(debug=True)
