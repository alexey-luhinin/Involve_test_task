'''Forms'''
from wtforms import (
    Form,
    DecimalField,
    SelectField,
    TextAreaField
)

from config import Currency

class PayForm(Form):
    amount = DecimalField('Сумма оплаты')
    currency = SelectField('Валюта оплаты',
                           choices=[(Currency.EUR.value, Currency.EUR.name),
                                    (Currency.USD.value, Currency.USD.name),
                                    (Currency.RUB.value, Currency.RUB.name)])
    description = TextAreaField('Описание товара')
