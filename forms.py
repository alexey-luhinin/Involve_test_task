'''Forms'''
from wtforms import (
    Form,
    DecimalField,
    SelectField,
    TextAreaField,
    SubmitField,
    HiddenField
)

from config import Currency

class PayForm(Form):
    amount = DecimalField('Сумма оплаты')
    currency = SelectField('Валюта оплаты',
                           choices=[(Currency.EUR.value, Currency.EUR.name),
                                    (Currency.USD.value, Currency.USD.name),
                                    (Currency.RUB.value, Currency.RUB.name)])
    description = TextAreaField('Описание товара')
    shop_id = HiddenField(default=5)
    shop_order_id = HiddenField(default=101)
    sign = HiddenField(default='')
