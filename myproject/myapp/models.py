from django.db import models

# Create your models here.
# myapp/models.py
from mongoengine import Document, StringField, IntField

class Book(Document):
    title = StringField(required=True, max_length=200)
    author = StringField(required=True)
    pages = IntField()
