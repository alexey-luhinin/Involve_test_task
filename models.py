'''Models'''
from datetime import datetime
from peewee import (
    SqliteDatabase,
    Model,
    PrimaryKeyField,
    IntegerField,
    FloatField,
    CharField,
    TextField,
    DateTimeField
)

db = SqliteDatabase('payments.db')


class Payment(Model):
    '''Payment model'''
    id = PrimaryKeyField(unique=True)
    date = DateTimeField(default=datetime.now())
    currency = IntegerField()
    amount = FloatField()
    shop_order_id = CharField()
    description = TextField()

    class Meta:
        database = db
