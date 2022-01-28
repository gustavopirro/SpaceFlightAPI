from rest_framework import generics
from api.models import Article
from api.models import Launch
from api.models import Event
from api.serializers import ArticleSerializer
from api.serializers import LaunchSerializer
from api.serializers import EventSerializer


class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class LaunchList(generics.ListCreateAPIView):
    queryset = Launch.objects.all()
    serializer_class = LaunchSerializer


class LaunchDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Launch.objects.all()
    serializer_class = LaunchSerializer


class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
