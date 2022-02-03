from django.http import HttpResponse
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

    def post(self, request, *args, **kwargs):
        self.serializer_class.create(self, validated_data=request.data, *args, **kwargs)
        return HttpResponse('Update finished sucessfully.', status=200)


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def put(self, request, *args, **kwargs):
        self.serializer_class.create(self, validated_data=request.data, *args, **kwargs)
        return HttpResponse('Update finished sucessfully.', status=200)


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
