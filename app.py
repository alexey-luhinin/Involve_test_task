'''Views'''
from flask import (
    Flask,
    render_template,
    request,
    jsonify,
)
from config import Currency
from payments_handler import eur_handler, usd_handler, rub_handler

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_request = request.get_json()
        currency = user_request['currency']

        if currency == str(Currency.EUR.value):
            return jsonify(eur_handler(user_request))

        if currency == str(Currency.USD.value):
            return jsonify(usd_handler(user_request))

        if currency == str(Currency.RUB.value):
            return jsonify(rub_handler(user_request))

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
