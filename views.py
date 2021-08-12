from flask import (
    render_template,
    request,
    jsonify,
)

from app import app
import config
from payments_handler import eur_handler, usd_handler, rub_handler


@config.logger.catch
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_request = request.get_json()
        currency = user_request['currency']

        if currency == str(config.Currency.EUR.value):
            return jsonify(eur_handler(user_request))

        if currency == str(config.Currency.USD.value):
            return jsonify(usd_handler(user_request))

        if currency == str(config.Currency.RUB.value):
            return jsonify(rub_handler(user_request))

    return render_template('index.html')
