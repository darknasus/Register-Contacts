import peewee

from app.v1.utils.db import db

class User(peewee.Model):
    name               = peewee.CharField()
    last_name          = peewee.CharField()
    address            = peewee.CharField()
    email              = peewee.CharField()
    phone              = peewee.IntegerField()
    twitter            = peewee.CharField()
    facebook           = peewee.CharField()
    instagram          = peewee.CharField()
    allowed_whatsapp   = peewee.BooleanField(default=False)


    class Meta:
        database = db