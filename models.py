from datetime import datetime
from peewee import (
    SqliteDatabase,
    Model,
    AutoField,
    IntegerField,
    FloatField,
    CharField,
    TextField,
    DateTimeField
)

db = SqliteDatabase('payments.db')


class Payment(Model):
    id = AutoField()
    date = DateTimeField(default=datetime.now())
    currency = IntegerField()
    amount = FloatField()
    shop_order_id = CharField()
    description = TextField()

    class Meta:
        database = db
