'''Forms'''
from wtforms import (
    Form,
    DecimalField,
    SelectField,
    TextAreaField,
    SubmitField
)

from wtforms.validators import InputRequired

from config import Currency

class PayForm(Form):
    class Meta:
        locales = ('ru_RU', 'ru')
    amount = DecimalField('Сумма оплаты:', validators=[InputRequired()])
    currency = SelectField('Валюта оплаты:',
                           choices=[(Currency.EUR.value, Currency.EUR.name),
                                    (Currency.USD.value, Currency.USD.name),
                                    (Currency.RUB.value, Currency.RUB.name)])
    description = TextAreaField('Описание товара:')
    submit = SubmitField('Оплатить')
