from django.db import models


class Event(models.Model):
    provider = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.provider


class Launch(models.Model):
    provider = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.provider


class Article(models.Model):
    title = models.CharField(max_length=150)
    url = models.URLField()
    imageUrl = models.URLField()
    newsSite = models.CharField(max_length=100)
    featured = models.BooleanField(default=False)
    summary = models.CharField(max_length=300)
    publishedAt = models.DateTimeField()
    updatedAt = models.DateTimeField()
    launches = models.ManyToManyField(Launch, blank=True)
    events = models.ManyToManyField(Event, blank=True)

    def __str__(self) -> str:
        return self.title
