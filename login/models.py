from django.db import models
from django.db.models import CharField


class User(models.Model):
    account = CharField(max_length=255)
    password = CharField(max_length=255)
