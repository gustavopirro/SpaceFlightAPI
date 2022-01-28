from django.db import models
from django.forms import BooleanField, CharField, DateTimeField, URLField


class Event(models.Model):
    provider = CharField(max_length=100)


class Launch(models.Model):
    provider = CharField(max_length=100)


class Article(models.Model):
    title = CharField(max_length=150)
    url = URLField()
    imageUrl = URLField()
    newsSite = CharField(max_length=100)
    featured = BooleanField(initial=False)
    summary = CharField(max_length=300)
    publishedAt = DateTimeField()
    updatedAt = DateTimeField()
    launches = models.ManyToManyField(Launch, blank=True)
    events = models.ManyToManyField(Event, blank=True)
