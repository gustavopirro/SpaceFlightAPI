from rest_framework import generics
from rest_framework import permissions
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
    permission_classes = [permissions.IsAuthenticated]
    queryset = Launch.objects.all()
    serializer_class = LaunchSerializer


class LaunchDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Launch.objects.all()
    serializer_class = LaunchSerializer


class EventList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Event.objects.all()
    serializer_class = EventSerializer
