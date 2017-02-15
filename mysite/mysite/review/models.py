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

class Evaluation(Document):
    positiv_false = ListField()
    the_neutral_accuracy = FloatField()
    timestamp = StringField()
    false_neutral_count = IntField()
    true_neutral_count = IntField()
    false_negativ_count = IntField()
    neutral_false = ListField()
    the_total_accuracy = FloatField()
    the_negativ_accuracy = FloatField()
    false_positiv_count = IntField()
    negativ_false = ListField()
    true_negativ_count = IntField()
    the_positiv_accuracy = FloatField()
    true_positiv_count = IntField()
    review_count = IntField()
    #Title only
    title_the_neutral_accuracy = FloatField()
    title_false_neutral_count = IntField()
    title_true_neutral_count = IntField()
    title_false_negativ_count = IntField()
    title_the_total_accuracy = FloatField()
    title_the_negativ_accuracy = FloatField()
    title_false_positiv_count = IntField()
    title_true_negativ_count = IntField()
    title_the_positiv_accuracy = FloatField()
    title_true_positiv_count = IntField()
    #Content only
    content_the_neutral_accuracy = FloatField()
    content_false_neutral_count = IntField()
    content_true_neutral_count = IntField()
    content_false_negativ_count = IntField()
    content_the_total_accuracy = FloatField()
    content_the_negativ_accuracy = FloatField()
    content_false_positiv_count = IntField()
    content_true_negativ_count = IntField()
    content_the_positiv_accuracy = FloatField()
    content_true_positiv_count = IntField()
