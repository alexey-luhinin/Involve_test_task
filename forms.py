from wtforms import Form, DecimalField, SelectField, TextAreaField, SubmitField

class PayForm(Form):
    amount = DecimalField('Сумма оплаты')
    currency = SelectField('Валюта оплаты')
    description = TextAreaField('Описание товара')
    submit = SubmitField('Оплатить')
