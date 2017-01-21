from __future__ import unicode_literals
from django.db import models
from mongoengine import *
# Fields of Mongoengine
# StringField(regex=None, max_length=None, min_length=None, **kwargs)
#
# URLField(verify_exists=False, url_regex=None, schemes=None, **kwargs)
#
# EmailField(regex=None, max_length=None, min_length=None, **kwargs)
#
# IntField(min_value=None, max_value=None, **kwargs)
#
# FloatField(min_value=None, max_value=None, **kwargs)
#
# DecimalField(min_value=None, max_value=None, force_string=False, precision=2,
# rounding='ROUND_HALF_UP', **kwargs)
# Create your models here.
# class Employee(Document):
#     email = StringField(required=True)
#     first_name = StringField(max_length=50)
#     last_name = StringField(max_length=50)

class Reviews(Document):
    # _id = IntField(primary_key=True)
    content_lenght = IntField()
    title_score = IntField()
    content_eval = StringField()
    review_stars = FloatField()
    hotel_name = StringField()
    review_score = IntField()
    city = StringField()
    helpful_reader = IntField()
    title = StringField()
    content_score = IntField()
    stars_eval = StringField()
    content = StringField()
    title_eval = StringField()
    review_eval = StringField()
