import json
from flask import Flask, render_template, request, redirect, jsonify
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

        # user_request = json.loads(request.data.decode())
        # currency = user_request['currency']

            keys_sorted = sorted(eur_payment.required_fields)
            values = [user_request.get(key) for key in keys_sorted]
            sign = list_to_str(values) + SECRET
            sign_hashed = get_sha256(sign)
            print(sign, sign_hashed)

            response = dict(zip(keys_sorted, values))
            response['sign'] = sign_hashed
            response['uri'] = eur_payment.uri

            return jsonify(response)

    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
