from django.db import models


class Event(models.Model):
    id = models.CharField(max_length=150, primary_key=True)
    provider = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.provider


class Launch(models.Model):
    id = models.CharField(max_length=150, primary_key=True)
    provider = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.provider


class Article(models.Model):
    title = models.CharField(max_length=150)
    url = models.URLField(max_length=600)
    imageUrl = models.URLField(max_length=600)
    newsSite = models.CharField(max_length=100)
    featured = models.BooleanField(default=False)
    summary = models.TextField(blank=True)
    publishedAt = models.DateTimeField()
    updatedAt = models.DateTimeField()
    launches = models.ManyToManyField(Launch, blank=True)
    events = models.ManyToManyField(Event, blank=True)

    def __str__(self) -> str:
        return self.title
